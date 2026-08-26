from fastapi import FastAPI
from app.api.search import router as search_router


app = FastAPI(
    title="AI Job Search Agent",
    version="0.1.0"
)

app.include_router(
    search_router,
    prefix="/api"
)