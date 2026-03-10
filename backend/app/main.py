from fastapi import FastAPI

from backend.app.routes.auth import auth_router
from backend.app.routes.route import router
app = FastAPI()
app.include_router(router)
app.include_router(auth_router)