from infrastructure.databases.mongodb.comment import Comment_DB
from infrastructure.databases.mongodb.job_post import Job_Post_DB
from infrastructure.databases.mongodb.rating import Rating_DB
from infrastructure.databases.mongodb.request import Request_DB
from infrastructure.databases.mongodb.unban_request import Unban_Request_DB
from infrastructure.databases.mongodb.user import User_DB
from infrastructure.databases.mongodb.vote import Vote_DB

"""
Factory class for generating databases
"""
class DB_Factory:
    async def comment():
        comment_db = Comment_DB()
        await comment_db.setup_collection()
        return comment_db

    async def job_post():
        job_post_db = Job_Post_DB()
        await job_post_db.setup_collection()
        return job_post_db

    async def rating():
        rating_db = Rating_DB()
        await rating_db.setup_collection()
        return rating_db

    async def request():
        request_db = Request_DB()
        await request_db.setup_collection()
        return request_db

    async def unban_request():
        unban_request_db = Unban_Request_DB()
        await unban_request_db.setup_collection()
        return urban_request_db

    async def user():
        user_db = User_DB()
        await user_db.setup_collection()
        return user_db

    async def vote():
        vote_db = Vote_DB()
        await vote_db.setup_collection()
        return vote_db