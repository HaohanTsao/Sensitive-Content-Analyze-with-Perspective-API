import os
import uvicorn
from fastapi import FastAPI
from src.api.api_v1.router import router_v1
from src.api.api_v1.endpoints import content_censor
from src.configs.config import get_config
from dotenv import load_dotenv

load_dotenv()
config = get_config()

app = FastAPI()
app.include_router(router_v1, prefix="/supabase_webhook_handler")


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=config.DEBUG)


if __name__ == "__main__":
    main()
