from registries.databases.db_factory import DB_Factory
from registries.databases.db_registry import DB_Registry

"""
Function for setting up the registry 
"""
async def setup_db_registry():
    factory = DB_Factory()
    registry = DB_Registry()

    comment = await factory.comment()
    registry.register_db('comment' , comment)

    job_post = await factory.job_post()
    registry.register_db('job_post' , job_post)

    rating = await factory.rating()
    registry.register_db('rating' , rating)

    request = await factory.request()
    registry.register_db('request' , request)

    unban_request = await factory.unban_request()
    registry.register_db('unban_request' , factory.unban_request)

    user = await factory.user()
    registry.register_db('user' , user)

    vote = await factory.vote()
    registry.register_db('vote' , factory.vote)
    
    return regisry