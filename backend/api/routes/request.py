import logging

from infrastructure.jwt import Jwt_Manager
from fastapi import APIRouter, Request, status, HTTPException, Depends, BackgroundTasks

from helpers.ratelimiter import limiter

router = APIRouter()

logger = logging.getLogger(__name__)

@limiter.limit("")
@router.get("/get_request")
async def 