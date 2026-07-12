from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
import logging

from api.schemas.auth import User

"""
Class for managing the MongoDB instance
"""
class MongoDB_Manager:
    """
    Constructor for the MongoDB manager.
    Params: None
    """
    def __init__ (self):
        db_username = os.getenv("MONGODB_USERNAME")
        db_password = os.getenv('MONGODB_PASSWORD')
        self.uri = f"mongodb+srv://{db_username}:{db_password}@jobrate.67izimm.mongodb.net/?appName=JobRate"
        self.logger = logging.getLogger(__name__)

    """
    Function for getting the table that one is using
    Params: table (str) -- name of the table
    Returns: table object 
    """
    def get_collection(self, table: str):
        uri = self.uri

        try:
            client = MongoClient(uri, server_api=ServerApi('1'))
            db = client["Job_Post_Rating"]
            return db[table]
        except Exception as e:
            self.logger.error(f"Something has gone wrong while getting the mongodb table: {str(e)}")
            raise RuntimeError("Something has gone wrong while getting the mondodb table")

    """
    Function for setting up the user table
    """
    def setup_user_collection(self):
        users_collection = self.get_collection("users")
        users_collection.create_index("username", unique=True)

    """
    Function to create the database
    """
    def add_user(self, user : User):
        user_collection = self.get_collection("users")

        user_object = dict(user)

        try:
            user = user_collection.insert_one(user_object)
            return user.inserted_id
        except DuplicateKeyError as e:
            self.logger.error(f"This username already exists: {str(e)}")
            raise DuplicateKeyError("This username already exists")
        except Exception as e:
            self.logger.error(f"An error occured while inserting a user: {str(e)}")
            raise RuntimeError("An error occured while inserting a user")

    """
    Function to test he connction of the mongodb manager.
    Params: None
    Returns: None
    """
    def test (self):
        uri = self.uri
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(f"Something went wrong: {str(e)}")

if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(filename='job_post_rating.log', level=logging.INFO)
    user = User(username="watsonian132", password="testingtestingtesting123")
    mongodb = MongoDB_Manager()
    mongodb.setup_user_collection()
    mongodb.add_user(user)