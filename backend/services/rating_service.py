from infrastructure.databases.mongodb.rating import Rating_DB
from infrastructure.databases.mongodb.job_post import Job_Post_DB

from schemas.services.rating import Rating, Rating_Identifiers

"""
Class for managing the ratings service logic
"""
class Ratings_Service:
    def __init__ (self, rating : Rating_DB, job_post : Job_Post_DB):
        self.rating = rating.collection
        self.job_post = job_post.collection
        self.db = rating

    """
    Function for upserting ratings
    Params: rating (Rating)
    Returns: whether an entry was created or updated
    """
    async def upsert_rating(self, rating : Rating):
        async def helper():
            search_query = {"user_id" : rating.user_id, "job_post_id" : rating.job_post_id}

            old_rating_doc = await self.rating.find_one_and_update(
                search_query,
                {"$set": rating.model_dump()},
                upsert=True,
                return_document=ReturnDocument.BEFORE  # Gives us the snapshot right before the overwrite
            )

            if not old_rating_doc:
                await self.job_post.update_one({"_id" : rating.job_post_id},
                                                {"$inc" : {"vote_sum" : rating.rating,
                                                            "vote_count" : 1}})
                return True

            rating_difference = rating.rating - old_rating_doc['rating']

            if rating_difference != 0:
                await self.job_post.update_one({"_id" : rating.job_post_id}, 
                                                {"$inc" : {"vote_sum": (rating.rating - old_rating_doc['rating'])}})
            return True

        return await self.db.start_transaction(helper)
        

    """
    Function that edits a rating for the user
    Params: rating_ids (Ratings_Identifiers)
    Returns: whether an entry was found
    """
    async def get_user_rating(self, rating_ids: Rating_Identifiers):
        return await self.rating.find_one(rating_ids)

    """
    Function for removing user ratings
    Params: rating_ids (Ratings_Identifiers)
    Returns: whether an entry was deleted
    """
    async def remove_user_rating(self, rating_ids : Rating_Identifiers):
        result = await self.rating.delete_one(rating_ids.model_dump())
        return result.deleted_count > 0