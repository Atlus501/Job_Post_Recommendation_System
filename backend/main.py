from fastapi import FastAPI, APIRouter, status
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
import uvicorn
from dotenv import load_env
import os

from api.routes.auth import router as auth_router

from services.auth.authmanager import Auth_Manager

allowed_origins = [
    "http://localhost:8000", # If you also test locally
]

#creating dependencies 
@asynccontextmanager
async def lifespan(app: FastAPI):
    # [Startup]: Triggered before the server starts accepting requests
    logging.basicConfig(level=logging.WARNING, filename="job_post_recommendation_system.log", 
                                               format='%(asctime)s - %(levelname)s - %(message)s')
    app.state.auth_manager = Auth_Manager()

    yield

    logging.warning("shutting off services")

#app
app = FastAPI(
    title="job recommendation backend"
    lifespan=lifespan,
    description="Asynchronous backend service managing text context vector lookups",
    version="1.0.0"
)

#adding cors middlware
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,           # Allowed domains list
    allow_credentials=True,          # Permit cookies / auth headers
    allow_methods=["*"],             # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],             # Allow all custom HTTP headers
)

app.include_router(auth_router, prefix="/auth")

"""
Function that initially welcomes the user as the are connected to the endpoint.
"""
@app.get("/", status_code=status.HTTP_200_OK)
async def respond():
    response_body = {
        "response" : "you have been connected",
    }
    return response_body

if __name__ = "__main__":
    logging.info("starting services")
    load_env()

    SERVER_IP = os.getenv("SERVER_IP")
    SERVER_PORT = int(os.getenv("SERVER_PORT"))
    uvicorn.run("main:app", host=SERVER_IP, port=SERVER_PORT, reload=True)