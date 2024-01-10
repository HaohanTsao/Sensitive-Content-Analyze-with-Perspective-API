import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("SUPABASE_API_URL")
key: str = os.environ.get("SUPABASE_API_PUBLIC_KEY")
supabase: Client = create_client(url, key)

# SELECT with filter

data, count = (
    supabase.table("posts")
    .select("*")
    .eq("id", "e69de0fb-c98c-428c-a2ea-7e0f862cd400")
    .execute()
)
print(data)

# update row with id
