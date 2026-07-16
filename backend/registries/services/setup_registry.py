from registries.services.service_factory import Service_Factory
from registries.services.service_registry import Service_Registry

"""
Function that setups up and returns a functional registry
"""
def setup_service_registry():
    factory = Service_Factory()
    registry = Service_Registry()

    regsitry['auth'] = factory.auth()
    registry['comment'] = factory.comment()
    registry['job_post'] = factory.job_post()
    registry['rating'] = factory.rating()
    registry['request'] = factory.request()
    registry['unban_request'] = factory.unban_request()
    registry['vote'] = factory.vote()

    return registry