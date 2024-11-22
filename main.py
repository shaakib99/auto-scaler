from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from worker_service.route import router as worker_router
from port_service.route import router as port_router
from worker_discovery_service.route import router as service_discovery_router
from metrics_service.route import router as metrics_router
from environment_variable_service.route import router as environment_variable_router
from common.middlewares import ResponseMiddleware, LoggingMiddleware
from database_service.mysql_service import MySQLDatabaseService

async def lifespan(app):
    # load env
    load_dotenv()
    await MySQLDatabaseService.get_instance().create_metadata()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(LoggingMiddleware)
app.add_middleware(ResponseMiddleware, excluded_paths = ['/services', '^/[^/]+/metrics$'])

routers: list[APIRouter] = [
    worker_router, 
    port_router, 
    environment_variable_router, 
    service_discovery_router, 
    metrics_router
    ]
for router in routers:
    app.include_router(router)

@app.get("/")
async def hello():
    return "hello"