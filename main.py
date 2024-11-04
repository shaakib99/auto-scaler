from fastapi import FastAPI

async def lifespan(app):
    yield

app = FastAPI(lifespan=lifespan)