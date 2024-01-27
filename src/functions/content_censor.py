import os
from src.services.perspective_api.censor import Censor
from src.services.slack.send_message import send_slack_message
from src.services.supabase.table_functions import update_table, get_table
from src.services.email.send_email import send_email
import logging
import functions_framework
from dotenv import load_dotenv

load_dotenv()
censor = Censor(
    api_key=os.getenv("GCP_API_KEY"), sensitive_keywords=["約炮", "約砲", "外送茶"]
)


"""
supabase webhook payload:

type InsertPayload = {
  type: 'INSERT'
  table: string
  schema: string
  record: TableRecord<T>
  old_record: null
}
type UpdatePayload = {
  type: 'UPDATE'
  table: string
  schema: string
  record: TableRecord<T>
  old_record: TableRecord<T>
}
type DeletePayload = {
  type: 'DELETE'
  table: string
  schema: string
  record: null
  old_record: TableRecord<T>
}
"""


@functions_framework.http
def content_censor(req):
    # get post info
    req = req.get_json(silent=True)
    id = req["record"].get("id")
    raw_content = req["record"].get("content_raw")
    raw_title = req["record"].get("title_raw")
    full_post = raw_title + "\n" + raw_content

    if full_post:
        # censor post
        censor_result = censor.analyze(content=full_post, threshhold=0.5)

    else:
        logging.error("post is null with id: %s", id)

    # check if post is sensitive
    is_sensitive = censor_result["is_sensitive"]
    if is_sensitive:
        # change is_deleted to True
        update_table(
            table_name=req["table"],
            update_info={"is_deleted": True},
            conditions={"id": id},
        )

        # notify managers through slack
        msg_to_admin = f"""Dectected a post with sensitive content:

post_id: {id}
user_id: {req["record"].get("user_id")}
toxic_score: {censor_result["toxic_score"]}
reseasons: {censor_result["reasons"]}
title: {raw_title}
content:
{raw_content}

"""
        send_slack_message(msg_to_admin)

    #         # notify user
    #         user_email = get_table(
    #             "profiles", conditions={"id": req["record"].get("user_id")}
    #         )[1][0].get("email")

    #         msg_to_user = """
    # 親愛的用戶:

    # 我們在您的貼文中偵測出敏感內容，目前暫時從頁面中移除，我們會在確認後決定是否恢復貼文。

    # OfferLand 敬上
    # """

    #         send_email(
    #             os.getenv("EMAIL"),
    #             os.getenv("EMAIL_APP_PASSWORD"),
    #             user_email,
    #             "Sensitive Content Alert",
    #             msg_to_user,
    #         )

    #         return {"status_code": 200, "is_sensitive": True}

    else:
        logging.info("post with id: %s passed content censor", id)
        return {"status_code": 200, "is_sensitive": False}
