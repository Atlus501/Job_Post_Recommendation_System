from fastapi import Request, status
from fastapi.responses import JSONResponse

import logging

from pymongo.errors import DuplicateKeyError

logger = logging.getLogger(__name__)

"""
Global error handler for duplciate key exceptions
"""
def duplicate_key_error_handler(request: Request, e: DuplicateKeyError):
    logger.error(f"Duplicate key detected! {str(e)}")

    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"detail" : "You have declared a key that already exists. Try another value"}
    )