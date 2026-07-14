import logging

from infrastructure.databases.mongodb.requests import Requests_Manager
from api.schemas.requests import Request

"""
Class for business logic of managing requests
"""
class Requests_Manager:
    """
    Constructor for managing requests to add job postings
    """
    def __init__(self, db : Requests_Manager)
        self.client = db.client
        self.collection = db.collection

    """
    Function for adding requests
    """
    async def add_request(self, request: Request):
        request_data = request.model_dump()
        return await self.collection.insert_one(request_data)

    """
    Function for retrieving a batch of requests
    """
    async def get_request_batch(self, session, reviewer, limit=20):
        async with self.client.start_session().bind():
            docs = await self.collection.find({"reviewed" : False, "reviewer" : {"$exists" : False}}).limit(limit).sort("create_date", pymongo.ASCENDING)
            doc_list = await docs.to_list()
            if doc_list == []:
                return []

            ids = [doc['_id'] for doc in doc_list]
            await self.collection.update_many({"_id" : {"$in" : ids}}, {"$set" : {"reviewer" : reviewer}})
            return doc_list

    """
    Function for reviewing a request
    Params: id (str) -- id string of the document
            approved (bool) -- status of whether the request is approved
    Returns: status (bool) -- whether it has successfully updated the request
    """
    async def review_request(self, id : str, approved : bool):
        result = await self.collection.update_one({"_id" : id}, {"$set" : {"approved" : approved}})
        return result.matched_count > 0
    
    """
    Function for deleting requests
    Params: None

    """
    async def delete_unverified_requests(self):
        return await self.collection.delete_many({"approved" : False, "reviewer" : {"$exists" : True}}, 
                                                    comment="removing denied requests")