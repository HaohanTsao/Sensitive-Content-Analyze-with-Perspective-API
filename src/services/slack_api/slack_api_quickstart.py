# %%
import logging

logging.basicConfig(level=logging.DEBUG)

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()

# %%
slack_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token=slack_token)

channel_name = "sensitive_post_notification"
conversation_id = None

# %%
try:
    # Call the conversations.list method using the WebClient
    for result in client.conversations_list():
        if conversation_id is not None:
            break
        for channel in result["channels"]:
            if channel["name"] == channel_name:
                conversation_id = channel["id"]
                # Print result
                print(f"Found conversation ID: {conversation_id}")
                break

except SlackApiError as e:
    print(f"Error: {e}")

# %%

# Notice: 記得邀請你建立的SLACK BOT (app)進入channel
try:
    # Call the conversations.list method using the WebClient
    result = client.chat_postMessage(channel=conversation_id, text="Hello world!")
    # Print result, which includes information about the message (like TS)
    print(result)

except SlackApiError as e:
    print(f"Error: {e}")
