import logging

import pymongo

from schemas.services.request import Request

from infrastructure.databases.mongodb.request import Request_DB

"""
Class for business logic of managing requests
"""
class Request_Service:
    """
    Constructor for managing requests to add job postings
    """
    def __init__(self, db : Request_DB):
        self.db = db
        self.request = db.collection

    """
    Function for adding requests
    """
    async def add_request(self, request: Request):
        request_data = request.model_dump()
        return await self.request.insert_one(request_data)

    """
    Function for retrieving a batch of requests
    """
    async def get_request_batch(self, reviewer, limit=20):
        async def helper():
            docs = await self.request.find({"reviewed" : False, "reviewer" : {"$exists" : False}}).limit(limit).sort("create_date", pymongo.ASCENDING)
            doc_list = await docs.to_list()
            if doc_list == []:
                return []

            ids = [doc['_id'] for doc in doc_list]
            await self.request.update_many({"_id" : {"$in" : ids}}, {"$set" : {"reviewer" : reviewer}})
            return doc_list

        return await self.db.start_transaction(helper)

    """
    Function for reviewing a request
    Params: id (str) -- id string of the document
            approved (bool) -- status of whether the request is approved
    Returns: status (bool) -- whether it has successfully updated the request
    """
    async def review_request(self, id : str, approved : bool):
        result = await self.request.update_one({"_id" : id}, {"$set" : {"approved" : approved}})
        return result.modified > 0
    
    """
    Function for deleting requests
    Params: None

    """
    async def delete_unverified_requests(self):
        result = await self.request.delete_many({"approved" : False, "reviewer" : {"$exists" : True}}, 
                                                    comment="removing denied requests")
        return result.deleted_count > 0