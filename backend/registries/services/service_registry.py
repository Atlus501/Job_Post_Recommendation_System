"""
Class for the services registry. Made to decouple service construction logic and 
maximize maintainability. 
"""
class Service_Registry:
    def __init__ (self):
        self.registry = {}

    """
    Register a callable (e.g., a factory method or lambda) that creates a guardrail.
    """
    def register_service(self, service_name: str, service):
        self.registry[service_name] = service

    """
    Get the creator function, which can then be called with specific arguments.
    """
    def get_db(self, service_name: str):
        if guardrail_type not in self.registry:
            raise ValueError(f"database type '{service_name}' not registered.")
        return self.registry[service_name]