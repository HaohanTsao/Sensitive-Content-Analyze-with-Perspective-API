echo "Deploying to gcloud..."

gcloud functions deploy supabase_webhook_handler \
--gen2 \
--runtime=python39 \
--region=asia-east1 \
--source=. \
--entry-point=main \
--trigger-http \
--allow-unauthenticated \
--no-user-output-enabled

echo "Deployed to gcloud!"