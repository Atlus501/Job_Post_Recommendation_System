from api.schemas.auth import User

from infrastructure.databases.mongodb import MongoDB_Manager

"""
Class for managing users in a mongodb database
"""
class User_Manager(MongoDB_Manager):
    def __init__ (self):
        super.__init__()

    """
    Function for setting up the user table
    """
    def setup_user_collection(self):
        users_collection = self.get_collection("users")
        users_collection.create_index("username", unique=True)