from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from worker_service.route import router as worker_router
from port_service.route import router as port_router
from environment_variable_service.route import router as environment_variable_router
from common.middlewares import ResponseMiddleware

async def lifespan(app):
    # load env
    load_dotenv()
    yield

app = FastAPI(lifespan=lifespan)

custom_middlewares = [{"priority": 1, "middleware": ResponseMiddleware}]

for middleware in sorted(custom_middlewares, key=lambda x: x["priority"]):
    app.add_middleware(middleware["middleware"])

routers: list[APIRouter] = [worker_router, port_router, environment_variable_router]
for router in routers:
    app.include_router(router)

@app.get("/")
async def hello():
    return "hello"