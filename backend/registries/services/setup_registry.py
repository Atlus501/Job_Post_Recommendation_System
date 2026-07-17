from registries.services.service_factory import Service_Factory
from registries.registry import Registry

from registries.databases.setup_registry import setup_db_registry

import asyncio

"""
Function that setups up and returns a functional registry
"""
async def setup_service_registry():
    db_registry = await setup_db_registry()

    factory = Service_Factory(db_registry)
    registry = Registry()

    registry.register('auth', factory.auth())
    registry.register('comment', factory.comment())
    registry.register('job_post', factory.job_post())
    registry.register('rating', factory.rating())
    registry.register('request', factory.request())
    registry.register('unban_request', factory.unban_request())
    registry.register('vote', factory.vote())

    return registry

if __name__ == "__main__":
    asyncio.run(setup_service_registry())