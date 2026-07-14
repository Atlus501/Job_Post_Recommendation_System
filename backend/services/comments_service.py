from datetime import datetime, timezone

from infrastructure.databases.mongodb.comments import Comments_DB
from infrastructure.databases.mongodb.ratings import Ratings_DB

from schemas.services.comments import Comment

"""
Class for handling comments related business logic
"""
class Comments_Service:
    """
    Constructor for comments service.
    Params: comments_db (Comments_DB)
            ratings_db (Ratings_DB)
    """
    def __init__ (self, comments_db : Comments_DB, ratings_db : Ratings_DB):
        self.comments = comments_db
        self.ratings = ratings_db

    """
    Retrieves a list of comments for a specific job
    """
    async def get_comments(self, job_post_id : str):
        result = await self.comments.find({"job_post_id" : job_post_id})
        return await result.to_list()

    async def add_comment(self, comment : Comment):
        user = comment.model_dump()
        user['upvotes'] = 0
        user['downvotes'] = 0
        user['created_date'] = str(datetime.now(timezone.utc))
        return await self.comment.insert(user)

    async def upsert_comment(self, comment : Comment):
        result = await self.comments.update_one({"user_id" : comment.user_id, "job_post_id" : job_post_id}, 
                                                {"$set" : {"description" : comment.description}})

        return result.modified_count > 0
