from pydantic import BaseModel


# Supabase webhook payload. Don't change.
class SupabaseInsertPayload(BaseModel):
    type: str  # should be 'INSERT'
    table: str
    schema: str
    record: dict
    old_record: dict  # should be null
