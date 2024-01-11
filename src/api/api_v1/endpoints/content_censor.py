import os
from fastapi import APIRouter
from services.content_censor.content_censor import Censor
from src.schemas.content_censor_schema import SupabaseInsertPayload
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
censor = Censor(
    api_key=os.getenv("GCP_API_KEY"), sensitive_keywords=["約炮", "約砲", "外送茶"]
)


@router.post("/content_censor")
async def censor_content(req: SupabaseInsertPayload):
    return
