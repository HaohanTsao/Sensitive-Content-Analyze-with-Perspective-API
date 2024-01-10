# %%
from src.censor.content_censor import Censor
from dotenv import load_dotenv
import pandas as pd
import os
import time

load_dotenv()

# %%
API_KEY = os.getenv("API_KEY")
SENSITIVE_KEYWORDS = ["外送茶", "約砲"]

post_df = pd.read_csv("data/posts_rows.csv")
content_censor = Censor(API_KEY, SENSITIVE_KEYWORDS)

post_df["full_post_raw"] = post_df["title_raw"] + "\n" + post_df["content_raw"]


def get_censor_score(row):
    try:
        output = content_censor.analyze(content=row["full_post_raw"], threshhold=0.5)
        time.sleep(1.1)
    except Exception as e:
        print(f"Error occurred: {e}")
        output = None

    return output


# %%
post_df["censor_output"] = post_df.apply(get_censor_score, axis=1)
post_df.to_csv("data/posts.csv", index=False)
# %%
post_df = post_df[post_df["censor_output"].notna()]
post_df["censor_score"] = post_df["censor_output"].apply(lambda x: x.get("toxic_score"))
post_df["censor_prediction"] = post_df["censor_output"].apply(
    lambda x: x.get("is_sensitive")
)
# %%
actual_values = post_df["is_deleted"]
predicted_values = post_df["censor_prediction"]

TP = 0
TN = 0
FP = 0
FN = 0

for actual, predicted in zip(actual_values, predicted_values):
    if actual == True and predicted == 1:
        TP += 1
    elif actual == 0 and predicted == 0:
        TN += 1
    elif actual == 0 and predicted == 1:
        FP += 1
    elif actual == 1 and predicted == 0:
        FN += 1

print(f"True Positive (TP): {TP}")
print(f"True Negative (TN): {TN}")
print(f"False Positive (FP): {FP}")
print(f"False Negative (FN): {FN}")
# %%
false_negative_data = post_df[
    (post_df["is_deleted"] == 1) & (post_df["censor_prediction"] == 0)
]
# %%
for index, row in false_negative_data.iterrows():
    print("=================================")
    print(row["full_post_raw"])
