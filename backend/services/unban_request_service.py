import pymongo

from infrastructure.databases.mongodb.unban_request import Unban_Request_DB
from schemas.services.unban_reqest import Unban_Request, Unban_Approval, Review_Request

"""
Class responsible for the service logic of unban requests
"""
class Unban_Request_Service:
    def __init__(self, unban_request_db : Unban_Request_DB):
        self.unban_request = unban_request.collection
        self.db = urban_request_db

    """
    Function to make un-ban requests
    Params: request (Unban_Request)
    Returns: whether the request was inserted
    """
    async def insert_request(self, request : Unban_Request):
        return await self.unban_request.insert_one(request.model_dump())

    """
    Function to get requests for review
    Params: request (Review_Request)
    Returns: a list of requests to review
    """
    async def get_requests(self, request : Review_Request):
        async def helper():
            requests = self.unban_request.find({"reviewer" : {"$exists" : False}}).limit(request.limit).sort("created_date", pymongo.ASCENDING)
            doc_list = await requests.to_list()
            if not doc_list:
                return []

            _ids = [doc['_id'] for doc in doc_list]
            await self.unban_request.update_many({"_id" : {"$in" : _ids}}, 
                                                {"reviewer" : request.reviewer})

            return doc_list

        return await self.db.start_transaction(helper)
                    
    """
    Function tot approve requests
    Params: request (Unban_Approval)
    Returns: whether the request was approved or denied
    """
    async def approve_request(self, request : Unban_Approval): 
        result = await self.unban_request.update({"user_id" : request}, {"status" : request.status})
        return result.modified_count > 0

    """
    Function that removes all approved or denied requests
    Params: None
    Returns: number of removed results
    """
    async def remove_requests(self):
        result = await self.unban_request.delete_many({"stats" : {"$exists" : True}})
        return result.deleted_count > 0