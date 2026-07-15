import infrastructure.databases.mongodb.rating import Rating_DB

from schemas.services.rating import Rating, Rating_Identifiers

"""
Class for managing the ratings service logic
"""
class Ratings_Service:
    def __init__ (self, db : Rating_DB):
        self.rating = db.collection
        self.client = db.client

    """
    Function for upserting ratings
    Params: rating (Rating)
    Returns: whether an entry was created or updated
    """
    async def upsert_rating(self, rating : Rating):
        result = await self.rating.update_one({user_id : rating.user_id, job_post_id : rating.job_post_id}, 
                                                    {"$set" : rating.model_dump()},
                                                    upsert=True)
        return result.modified_count > 0 or result.upserted_id is not None

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

    """
    Function that gets the average rating for a job post
    Params: job_post_id (str)
    Return: the average rating of a job position
    """
    async def get_avg_rating(self, job_post_id : str):
        result = awalt self.colelction.aggregate({"$match" : job_post_id}, 
                                                    {"$group" : {
                                                        _id : "$job_post_id",
                                                        "average_rating" : {"$avg" : "$rating"},
                                                    }})
        return result