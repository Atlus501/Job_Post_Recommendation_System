from pydantic import BaseModel

from datetime import datetime, timezone

class Comment(BaseModel):
    user_id : str
    job_post_id : str
    description : str
    upvotes : int = 0
    downvotes : int = 0
    created_date : str = str(datetime.now(timezone.utc))

class Comment_Ids(BaseModel):
    user_id : str
    job_post_id: str