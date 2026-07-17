from registries.services.service_factory import Service_Factory
from registries.services.service_registry import Service_Registry

from registries.databases.setup_registry import setup_db_registry

import asyncio

"""
Function that setups up and returns a functional registry
"""
async def setup_service_registry():
    db_registry = await setup_db_registry()

    factory = Service_Factory(db_registry)
    registry = Service_Registry()

    registry.register_service('auth', factory.auth())
    registry.register_service('comment', factory.comment())
    registry.register_service('job_post', factory.job_post())
    registry.register_service('rating', factory.rating())
    registry.register_service('request', factory.request())
    registry.register_service('unban_request', factory.unban_request())
    registry.register_service('vote', factory.vote())

    return registry

asyncio.run(setup_service_registry())