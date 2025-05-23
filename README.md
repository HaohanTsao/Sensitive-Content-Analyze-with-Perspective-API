# Sensitive-Content-Analyze-with-Perspective-API

Created a GCP Cloud Function named content_censor. Whenever a new post is inserted into Supabase, this function is triggered through a Supabase webhook. It checks for inappropriate content, and if the result of the check is true, the corresponding post is temporarily removed from the web, and a notification is sent to the administrators via Slack.

This project utilizes the Perspective API by Google to analyze sensitive content in text.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/HaohanTsao/Sensitive-Content-Analyze-with-Perspective-API.git
    cd Sensitive-Content-Analyze-with-Perspective-API
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Setting up API Key

1. Create a `.env` file in the root directory.

2. Add your environmental variables to the `.env` file:

    ```env
    GCP_API_KEY =
    SUPABASE_API_URL = 
    SUPABASE_API_PUBLIC_KEY = 
    SUPABASE_API_SECRET_KEY = 
    SLACK_BOT_TOKEN = 
    SLACK_CHANNEL_ID = 
    ```
## Usage
* Supabaase webhook: [https://supabase.com/docs/guides/database/webhooks]
* Supabase API: [https://supabase.com/docs/reference/python/initializing]
* Slack API: [https://api.slack.com/messaging/sending]
* GCP Cloud Function: [https://cloud.google.com/functions/docs/concepts/overview]
* Perspective API: [https://developers.perspectiveapi.com/s/docs-get-started?language=en_US]

## Deploy

```bash
    gcloud functions deploy content_censor --gen2 --runtime=python39 --region=asia-east1 --source=. --entry-point=main --trigger-http --allow-unauthenticated --no-user-output-enabled
```

## Test
### perspective_api test result with actual post data
Threshhold = 0.5, keywords: 外送茶、約砲

| Actual / Predicted | Predicted Positive (1) | Predicted Negative (0) |
|--------------------|------------------------|------------------------|
| Actual Positive (1) | 15 (TP)                | 2 (FN)                 |
| Actual Negative (0) | 0 (FP)                 | 230 (TN)               |

## Note
This project is in production for [OfferLand](https://offerland.cc/)
