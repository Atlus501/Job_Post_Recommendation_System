from infrastructure.databases.mongodb.mongodb import MongoDB

class Comment_DB(MongoDB):
    def __init__ (self):
        super.__init__()
        self.collection = self.get_collection("comments")

    async def setup_collection(self):
        await self.collection.create_index([("user_id", 1), ("job_post_id", 1)], unique=True)