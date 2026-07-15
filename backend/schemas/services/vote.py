from pydantic import BaseModel

class Vote(BaseModel):
    user_id : str
    comment_id : str
    upvote : bool