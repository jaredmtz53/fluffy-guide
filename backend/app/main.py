from fastapi import FastAPI

from backend.app.routes.route import router

app = FastAPI()
app.include_router(router)