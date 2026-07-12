import logging

from fastapi import APIRouter, Response, Request, status
from pydantic import ValidationError

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK)