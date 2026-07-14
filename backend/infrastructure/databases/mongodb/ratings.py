from infrastructure.databases.mongodb.mongodb import MongoDB

"""
Class for managing the ratings database
"""
class Ratings_DB(MongoDB):
    def __init__(self):
        super.__init__()
        self.collection = self.get_collection("ratings")

    def setup_collection(self):
        self.collection.create_index([("user_id" , 1), ("job_post_id", 1)], unique=True)