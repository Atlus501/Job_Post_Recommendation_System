from infrastructure.databases.mongodb import MongoDB_Manager

"""
Class for managing users in a mongodb database
"""
class User_Manager(MongoDB_Manager):
    def __init__ (self):
        super.__init__()
        self.collection = self.get_collection("users")

    """
    Function for setting up indicies in collection
    """
    async def setup_collection(self):
        await self.collection.create_index("username", unique=True)