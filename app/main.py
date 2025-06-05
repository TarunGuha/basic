import logging
from mangum import Mangum
from fastapi import FastAPI

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = FastAPI()
handler = Mangum(app)


@app.get("/")
async def root() -> str:
    return "Hello, world!"
