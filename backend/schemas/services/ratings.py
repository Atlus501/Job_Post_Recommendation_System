from pydantic import BaseModel

class Rating(BaseModel):
    user_id : str
    job_post_id : str
    rating : float

class Rating_Identifiers(BaseModel):
    user_id : str
    job_post_id : str