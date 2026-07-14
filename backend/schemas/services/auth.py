from pydantic import BaseModel

class User(BaseModel):
    username : str
    password : str
    banned : bool = False
    time_preference : "3 months"

class ChangePasswordInfo(BaseModel):
    username : str
    old_password : str
    new_password : str