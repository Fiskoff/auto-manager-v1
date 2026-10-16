from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, APIRouter

from backend.core.db_helper import DBHelper


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_helper = DBHelper()
    if not db_helper.has_tables():
        db_helper.create_tables()

    app.state.db_session_factory = db_helper.Session

    yield

    db_helper.engine.dispose()

app = FastAPI(lifespan=lifespan)

routers = APIRouter()
app.include_router(routers)


if __name__ == "__main__":
    uvicorn.run(app)