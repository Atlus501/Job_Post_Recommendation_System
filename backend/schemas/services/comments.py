from pydantic import BaseModel

class Comment(BaseModel):
    user_id : str
    job_post_id : str
    description : str

class Comment_Ids(BaseModel):
    user_id : str
    job_post_id: str