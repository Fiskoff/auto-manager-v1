from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, APIRouter

from backend.core.db_helper import DBHelper
from backend.app.routers import root_router, car_router, consumables_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_helper = DBHelper()
    app.state.db = db_helper

    if not db_helper.has_tables():
        db_helper.create_tables()

    app.state.db_session_factory = db_helper.Session

    yield

    db_helper.engine.dispose()

app = FastAPI(lifespan=lifespan)

routers = APIRouter()
routers.include_router(root_router)
routers.include_router(car_router)
routers.include_router(consumables_router)
app.include_router(routers)


if __name__ == "__main__":
    uvicorn.run(app)