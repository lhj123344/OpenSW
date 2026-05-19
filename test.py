from fastapi import FastAPI

from basic import router as basic_router
from auth import router as auth_router

app = FastAPI()
app.include_router(basic_router)
app.include_router(auth_router)

# 이 소스코드는 FastAPI를 이용한 웹 서버의 진입 코드입니다.