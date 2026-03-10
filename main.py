from fastapi import FastAPI
from database import engine
from models import Base

from routes import auth_routes
from routes import user_routes

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)
app.include_router(user_routes.router)