from registries.databases.db_factory import DB_Factory
from registries.registry import Registry

"""
Function for setting up the registry 
"""
async def setup_db_registry():
    factory = DB_Factory()
    registry = Registry()

    comment = await factory.comment()
    registry.register('comment', comment)

    job_post = await factory.job_post()
    registry.register('job_post', job_post)

    rating = await factory.rating()
    registry.register('rating', rating)

    request = await factory.request()
    registry.register('request', request)

    unban_request = await factory.unban_request()
    registry.register('unban_request', unban_request)

    user = await factory.user()
    registry.register('user', user)

    vote = await factory.vote()
    registry.register('vote', vote)
    
    return registry