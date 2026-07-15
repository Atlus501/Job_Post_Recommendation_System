from infrastructure.databases.mongodb.mongodb import MongoDB

class Unban_Request_DB(MongoDB):
    def __init__(self):
        super.__init__()
        self.collection = self.get_collection("unban_request")

    async def setup_collection(self):
        await self.collection.create_index("user_id", unique=True)