from infrastructure.databases.mongodb.mongodb import MongoDB

"""
Class for vote database. (upvotes or downvotes each user makes for each comment)
"""
class Vote_DB(MongoDB):
    def __init__ (self):
        super.__init__()
        self.collection = self.get_collection("votes")

    def setup_collection(self):
        self.collection.create_index([("user_id", 1), ("comment_id", 1)], unique=True)