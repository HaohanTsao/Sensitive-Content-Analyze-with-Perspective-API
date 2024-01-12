import logging

logging.basicConfig(level=logging.DEBUG)

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()

slack_token = os.getenv("SLACK_BOT_TOKEN")
channel_id = os.getenv("SLACK_CHANNEL_ID")
client = WebClient(token=slack_token)


def send_slack_message(text: str):
    try:
        # Call the conversations.list method using the WebClient
        result = client.chat_postMessage(channel=channel_id, text=text)
        # Print result, which includes information about the message (like TS)
        logging.info("Successfully sent slack message!\n")

    except SlackApiError as e:
        logging.error(e)

    return
