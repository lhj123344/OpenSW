from fastapi import FastAPI

from basic import router as basic_router
from auth import router as auth_router

app = FastAPI()
app.include_router(basic_router)
app.include_router(auth_router)