import os
from fastapi import APIRouter, HTTPException
from services.content_censor.content_censor import Censor
from src.services.slack.send_message import send_slack_message
from src.services.supabase.update_table import update_table
from src.schemas.content_censor_schema import SupabaseInsertPayload
import logging
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
censor = Censor(
    api_key=os.getenv("GCP_API_KEY"), sensitive_keywords=["約炮", "約砲", "外送茶"]
)


@router.post("/content_censor")
async def censor_content(req: SupabaseInsertPayload):
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
        raise HTTPException(status_code=400, detail="Invalid input: full_post is None")

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

    else:
        logging.info("post with id: %s passed content censor", id)
        return
