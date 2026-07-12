from pwdlib import PasswordHash

from services.auth.schemas import User

"""
This is the class that will manage the authentication information & jwt of users
"""
class Auth_Manager:
    """
    Constructor for the Auth_Manager
    """
    def __init__ (self, database):
        self.password_hash = PasswordHash.recommended()
        self.db = database

    """
    Function that hashes the password
    """
    def hash_password(self, userinfo):
        return self.password_hash.hash(password)

    """
    Function that retrieves the hashed password from the database based on the username
    """
    def get_stored_password(username):
        pass


    """
    Function that verifies the passwords 
    """
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)

    """
    Function that creates users and stores them in the database
    """
    def create_user(username: str, password: str):
        db.store({username, password})

    """
    Function that authenticates users
    """
    def authenticate_user(username: str, password: str):
    user = db.get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return True
