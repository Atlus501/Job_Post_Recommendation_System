from fastapi import FastAPI, APIRouter, status, HTTPException
from contextlib import asynccontextmanager
import logging
import uvicorn

from config.settings import settings

#middlewares
from middleware.secure_headers import SecureResponseMiddlware
from middleware.cors import setup_corsmiddleware

#routers
from api.routes.auth import router as auth_router

#error handler setup
from error_handling.setup_error_handlers import setup_error_handlers

#dependencies initiallized at beginning
from registries.services.setup_registry import setup_service_registry

from infrastructure.databases.neo4j import Neo4j_DB
from infrastructure.jwt import Jwt_Manager

#creating dependencies 
@asynccontextmanager
async def lifespan(app: FastAPI):
    # [Startup]: Triggered before the server starts accepting requests
    logging.basicConfig(level=logging.INFO, filename="job_post_recommendation_system.log", 
                                               format='%(asctime)s - %(levelname)s - %(message)s')

    app.state.service_registry = await setup_service_registry()
    app.state.neo4j_db = Neo4j_DB()

    app.state.jwt_manager = Jwt_Manager()

    yield

    logging.warning("shutting off services")

#app
app = FastAPI(
    title="job recommendation backend",
    lifespan=lifespan,
    description="Asynchronous backend service managing text context vector lookups",
    version="1.0.0"
)

#adding cors middlware
setup_corsmiddleware(app)
app.add_middleware(SecureResponseMiddlware)

app.include_router(auth_router, prefix="/auth")

setup_error_handler(app)

"""
Function that initially welcomes the user as the are connected to the endpoint.
"""
@app.get("/", status_code=status.HTTP_200_OK)
async def respond():
    response_body = {
        "response" : "you have been connected",
    }
    return response_body

if __name__ == "__main__":
    logging.info("starting services")

    SERVER_IP = settings.SERVER_IP
    SERVER_PORT = settings.SERVER_PORT
    uvicorn.run("main:app", host=SERVER_IP, port=SERVER_PORT, reload=True)