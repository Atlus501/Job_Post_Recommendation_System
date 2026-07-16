"""
Class for the registries that store information on creating databases
"""
class DB_Registry:
    def __init__ (self):
        self.registry = {}

    """
    Register a callable (e.g., a factory method or lambda) that creates a guardrail.
    """
    def register_db(self, db_name: str, db):
        self.registry[db_name] = db

    """
    Get the creator function, which can then be called with specific arguments.
    """
    def get_db(self, db_name: str):
        if guardrail_type not in self.registry:
            raise ValueError(f"database type '{db_name}' not registered.")
        return self.registry[db_name]

    