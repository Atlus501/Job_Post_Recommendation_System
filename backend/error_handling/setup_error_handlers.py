from fastapi import FastAPI
#errors
from registries.error_handlers.setup_error_handler_registry import setup_error_handler_registry

def setup_error_handlers(app : FastAPI):
    registry = setup_error_handler_registry()

    for value in registry.registry.values():
        app.add_exception_handler(value[0], value[1])

if __name__ == "__main__":
    app = FastAPI()
    setup_error_handler(app)