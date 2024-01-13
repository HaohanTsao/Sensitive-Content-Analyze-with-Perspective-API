import os
from src.services.perspective_api.censor import Censor
from src.services.slack.send_message import send_slack_message
from src.services.supabase.update_table import update_table
import logging
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


def content_censor(req):
    # get post info
    id = req.record.get("id")
    raw_content = req.record.get("content_raw")
    raw_title = req.record.get("title_raw")
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
            table_name=req.table,
            update_info={"is_deleted": True},
            conditions={"id": id},
        )

        # notify managers through slack
        message = f"""Dectected a post with sensitive content:

post_id: {id}
user_id: {req.record.get("user_id")}
toxic_score: {censor_result["toxic_score"]}
reseasons: {censor_result["reasons"]}"""

        send_slack_message(message)
        return {"status_code": 200, "is_sensitive": True}

    else:
        logging.info("post with id: %s passed content censor", id)
        return {"status_code": 200, "is_sensitive": False}
