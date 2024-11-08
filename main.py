from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from worker_service.route import router as worker_router
from port_service.route import router as port_router

async def lifespan(app):
    # load env
    load_dotenv()
    yield

app = FastAPI(lifespan=lifespan)

routers: list[APIRouter] = [worker_router, port_router]
for router in routers:
    app.include_router(router)