from src.censor.content_censor import Censor
import json
from dotenv import load_dotenv

load_dotenv()
import os

API_KEY = os.getenv("GCP_API_KEY")
SENSITIVE_KEYWORDS = []  # self-defined sensitive keywords
CONTENT = """Content to analyze
"""


def main():
    content_censor = Censor(api_key=API_KEY, sensitive_keywords=SENSITIVE_KEYWORDS)
    content = CONTENT

    output = content_censor.analyze(
        content=content, threshhold=0.5
    )  # threshhold could be [0,1], default 0.5
    output = json.dumps(output, indent=2, ensure_ascii=False)
    print(output)


if __name__ == "__main__":
    main()
