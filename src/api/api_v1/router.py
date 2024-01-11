from fastapi import APIRouter
from endpoints import content_censor

router_v1 = APIRouter()

router_v1.include_router(
    content_censor.router,
    prefix="/supabase_webhook_handler",
    tags=["supabase_webhook_handler"],
)
