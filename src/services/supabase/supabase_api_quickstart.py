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
query = supabase.table("posts").select("*").eq("is_deleted", False)

# multiple filters could be chained
query = query.eq("score", 80)
response = query.execute()
print(response)
