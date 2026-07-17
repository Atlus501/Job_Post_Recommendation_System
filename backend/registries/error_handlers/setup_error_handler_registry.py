from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError

from error_handling.error_handlers.authentication_handlers import invalid_token_error_handler
from error_handling.error_handlers.database_handlers import duplicate_key_error_handler
from error_handling.error_handlers.general_handlers import exception_handler, runtime_error_handler, http_exception_handler, validation_error_handler

from registries.registry import Registry

def setup_error_handler_registry():
    registry = Registry()

    registry.register('duplicate_key_error', (DuplicateKeyError, duplicate_key_error_handler))
    registry.register('exception', (Exception, exception_handler))
    registry.register('http_exception', (HTTPException, http_exception_handler))
    registry.register('invalid_token_error', (InvalidTokenError, invalid_token_error_handler))
    registry.register('runtime_error', (RuntimeError, runtime_error_handler))
    registry.register('validation_error', (ValidationError, validation_error_handler))

    return registry

if __name__ == "__main__":
    setup_error_handler_registry()