from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{"message" : "Hello FastAPI"}

@app.get("/add")
def add(a: int, b:int):
    return {"result" : a+b}

from pydantic import BaseModel

class Item(BaseModel):
    name : str
    price : int

@app.post("/item")
def create_item(item: Item):
    return {
        "name": item.name,
        "price" : item.price
    }

class User(BaseModel):
    name : str
    age : int

@app.post("/user")
def create_user(user:User):
    return {
        "message": f"{user.name} 등록완료",
        "age" : user.age
    }
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

from sqlalchemy import Column, Integer, String

class UserDB(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    Password = Column(String)

    Base.metadata.create_all(bind=engine)

    from sqlalchemy.orm import Session
    from fastapi import Depends

    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally : 
            db.close()

@app.post("/register")
def register(user: User, db: Session = Depends(get_db)):

    new_user = UserDB(
        username = user.name,
        password = "1234"
    )

    db.add(new_user)
    db.commit()

    return {"message" : "회원가입 완료"}
