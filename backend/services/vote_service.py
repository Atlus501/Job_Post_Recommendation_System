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

    """
    Function for upserting a vote
    Params: vote (Vote)
    Returns: result (bool) -- whether a vote was upserted
    """
    async def upsert_vote(self, vote : Vote):
        result = await self.vote.update_one({"user_id" : vote.user_id, "comment_id" : vote.comment_id}, 
                                        {"$set" : vote.model_dump()}, upsert=True)

        """
        Helper method for updating comment count
        """
        async def update_vote(upvote : bool):
            upvote_inc = 1 if upvote else -1
            return await self.comment.update_one({"_id" : vote.comment_id}, 
                                                        {"$inc": {"upvotes": upvote_inc,
                                                                    "downvotes" : -1 * upvote_inc}
                                                                    })

        async def update_inserted_vote(upvote : bool):
            field = "upvotes" if upvote else "downvotes"
            return await self.comment.update_one({"_id" : vote.comment_id},
                                                    {"$inc": {field : 1}})

        if result.modified_count > 0:
            await update_vote(vote.upvote)
            return True
        elif result.upserted_id is not None:
            await update_inserted_vote(vote.upvote)
            return True
                                
        return True

    """
    Function for getting a vote
    Params: user_id (str)
            comment_id (str)
    Returns: whether there was a vote 
    """
    async def get_user_vote(self, user_id : str, comment_id : str):
        return await self.vote.find_one({"user_id" : user_id, "comment_id" : comment_id})

    """
    Function for getting vote sum
    """
    async def get_comment_votes(self, comment_id : str):
        return await self.vote.aggregate({"$match" : comment_id}, 
                                        {"$group" : {_id : "$upvote", 
                                                        vote_count : {"$sum" : 1}}})