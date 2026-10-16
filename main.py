import uvicorn
from fastapi import FastAPI, APIRouter


app = FastAPI()
router = APIRouter()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app)