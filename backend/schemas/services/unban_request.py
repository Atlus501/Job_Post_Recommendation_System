from pydantic import BaseModel
from datetime import datetime, timezone

class Unban_Request(BaseModel):
    user_id: str
    reason: str
    created_date : str  = str(datetime.now(timezone.utc))

class Unban_Approval(BaseModel):
    user_id : str
    status : bool

class Review_Request(BaseModel):
    reviewer : str
    limit : int = 25