from fastapi import Request, status
from fastapi.responses import JSONResponse

import logging

from jwt.exceptions import InvalidTokenError

logger = logging.getLogger(__name__)

"""
Global error handler for invalid token errors
"""
def invalid_token_error_handler(request: Request, e : InvalidTokenError):
    logger.error(f"Invalid token was used! {str(e)}")

    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail" : "You have used an invalid jwt"}
    )