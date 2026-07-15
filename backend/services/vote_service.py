from infrastructure.databases.mongodb.vote import Vote_DB
from infrastructure.databases.mongodb.comment import Comment_DB

from schemas.services.vote import Vote

"""
Class for managing the business logic of voting
"""
class Vote_Service:
    """
    Constructor for the Vote_Service
    """
    def __init__(self, vote_db : Vote_DB, comment_db : Comment_DB):
        self.vote = vote_db.collection
        self.comment = comment_db.collection
        self.db = vote_db

    """
    Function for upserting a vote
    Params: vote (Vote)
    Returns: result (bool) -- whether a vote was upserted
    """
    async def upsert_vote(self, vote : Vote):
        async def helper():
            search_query = {"user_id": vote.user_id, "comment_id": vote.comment_id}

            old_doc = await self.vote.find_one_and_update(
                search_query,
                {"$set": vote.model_dump()},
                upsert=True,
                return_document=ReturnDocument.BEFORE
            )                

            if old_doc == None:
                field = "upvotes" if vote.upvote else "downvotes"

                await self.comment.update_one({"_id" : vote.comment_id},
                                                {"$inc": {field : 1}})
                return True

            if old_doc['upvote'] != vote.upvote:
                upvote_inc = 1 if upvote else -1
                await self.comment.update_one({"_id" : vote.comment_id}, 
                                                {"$inc": {"upvotes": upvote_inc,
                                                    "downvotes" : -1 * upvote_inc}
                                                })
                                    
            return True

        return await self.db.start_transaction(helper)

    """
    Function for getting a vote
    Params: user_id (str)
            comment_id (str)
    Returns: whether there was a vote 
    """
    async def get_user_vote(self, user_id : str, comment_id : str):
        return await self.vote.find_one({"user_id" : user_id, "comment_id" : comment_id})