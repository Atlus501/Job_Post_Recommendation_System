from datetime import datetime, timezone

from infrastructure.databases.mongodb.comment import Comment_DB
from infrastructure.databases.mongodb.vote import Vote_DB

from schemas.services.comments import Comment, Comment_Ids

"""
Class for handling comments related business logic
"""
class Comment_Service:
    """
    Constructor for comments service.
    Params: comments_db (Comments_DB)
            ratings_db (Ratings_DB)
    """
    def __init__ (self, comments_db : Comment_DB, vote_db : Vote_DB):
        self.comment = comments_db.collection

    """
    Retrieves a list of comments for a specific job.
    Params: job_post_id (str)
    Returns: list of comment objects
    """
    async def get_comments(self, job_post_id : str):
        result = await self.comment.find({"job_post_id" : job_post_id})
        return await result.to_list()

    """
    Adds a new comment
    Params: comment (Comment)
    Returns: result of whether the comment was inserted
    """
    async def add_comment(self, comment : Comment):
        return await self.comment.insert(comment.model_dump())

    """
    Inserts a new comment
    Params: comment (Comment)
    Returns: result of whether an entry was modified
    """
    async def upsert_comment(self, comment : Comment):
        result = await self.comment.update_one({"user_id" : comment.user_id, "job_post_id" : job_post_id}, 
                                                {"$set" : {"description" : comment.description}},
                                                upsert=True)
        return result.modified_count > 0

    """
    Removes a comment
    Params: comment_ids (Comment_ids)
    Returns: result of whether an entry was deleted
    """
    async def remove_comment(self, comment_ids : Comment_Ids):
        result = await self.comment.remove_one(comment_ids.model_dump())
        return result.deleted_count > 0
