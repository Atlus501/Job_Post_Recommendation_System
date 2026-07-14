import infrastructure.databases.mongodb.ratings import Ratings_DB

from schemas.services.ratings import Rating, Rating_Identifiers

"""
Class for managing the ratings service logic
"""
class Ratings_Service:
    def __init__ (self, db : Ratings_DB):
        self.collection = db.collection
        self.client = db.client

    """
    Function for updating ratings
    """
    async def upsert_rating(self, rating : Rating):
        result = await self.collection.update_one({user_id : rating.user_id, job_post_id : rating.job_post_id}, 
                                                    {"$set" : rating.model_dump()},
                                                    upsert=True)
        return result.modified_count > 0 or result.upserted_id is not None

    """
    Function that edits a rating for the user
    """
    async def get_user_rating(self, rating_ids: Rating_Identifiers):
        return await self.collection.find_one(rating_ids)

    """
    Function for removing user ratings
    """
    async def remove_user_rating(self, rating_ids : Rating_Identifiers):
        result = await self.collection.delete_one(rating_ids.model_dump())
        return result.deleted_count > 0