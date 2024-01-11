import os
import logging
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("SUPABASE_API_URL")
key: str = os.environ.get("SUPABASE_API_PUBLIC_KEY")
supabase: Client = create_client(url, key)


def update_table(table_name: str, update_info: dict, conditions: dict):
    try:
        query = supabase.table(table_name).update(update_info)

        for column, value in conditions.items():
            query = query.eq(column, value)

        data, count = query.execute()

        logging.info(
            f"Successfully updated {update_info} \n with condition {conditions} in table {table_name}"
        )
    except Exception as e:
        logging.error(f"Error updating table {table_name}: {str(e)}")