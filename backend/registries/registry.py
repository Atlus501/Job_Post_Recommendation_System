class Registry:
    def __init__ (self):
        self.registry = {}

    def register(self, name : str, object):
        self.registry[name] = object

    def get(self, name : str):
        if name not in self.registry:
            raise ValueError(f"object {str(name)} is not registered")
        return self.registry[name]
