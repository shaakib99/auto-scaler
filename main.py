from fastapi import FastAPI
from dotenv import load_dotenv

async def lifespan(app):
    # load env
    load_dotenv()
    yield

app = FastAPI(lifespan=lifespan)