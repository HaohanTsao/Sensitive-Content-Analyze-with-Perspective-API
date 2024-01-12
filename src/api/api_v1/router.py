from fastapi import APIRouter
from .endpoints import content_censor

router_v1 = APIRouter()

# add different version routers here if needed

router_v1.include_router(
    router=content_censor.router,
    prefix="/v1",
    tags=["supabase_webhook_handler_v1"],
)
