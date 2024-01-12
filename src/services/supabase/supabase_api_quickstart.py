# %%
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("SUPABASE_API_URL")
key: str = os.environ.get("SUPABASE_API_PUBLIC_KEY")
supabase: Client = create_client(url, key)

# %%
# api docs: https://supabase.com/docs/reference/python/introduction
# SELECT with filter
data, count = supabase.table("webhook_test").select("*").execute()
print(data)

# %%
# update
update_info = {"is_deleted": True}
data, count = supabase.table("webhook_test").update(update_info).eq("id", 1).execute()
