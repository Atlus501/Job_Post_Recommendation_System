from infrastructure.databases.mongodb.job_post import Job_Post_DB
from pymongo import InsertOne

from schemas.services.job_post import Job_Post

"""
Class that manages the service logic of job postings
"""
class Job_Post_Service:
    """
    Constructor for the job post service manager
    """
    def __init__ (self, db : Job_Post_DB):
        self.job_post = db.collection
        self.client = db.client

    """
    Function for getting job posts
    """
    async def get_job_posts(self, id_list : list[str]):
        res = await self.job_post.find({"_id" : {"$in" : id_list}}})
        return await res.to_list()
    
    """
    Function for bulk writing job posts
    """
    async def insert_job_posts(self, job_post_list : list[Job_Post]):
        if not job_post_list:
            return BulkWriteResult({}, acknowledged=True)

        requests = [InsertOne(document=job_post.model_dump()) for job_post in job_post_list]

        result = await self.job_post.bulk_write(requests, ordered=False)
        return result

    """
    Function for removing one job post
    """
    async def delete_job_post(self, id):
        result await self.job_post.delete_one({"_id" : id})
        return result.delete_count > 0

    """
    Function for updating one job post
    """
    async def update_job_post(self, id, job_post : Job_Post):
        result = await self.job_post.update_one({"_id" : id}, {"$set" : job_post.model_dump()})
        return result.modified_count > 0