from fastapi import FastAPI
from .routes import user
# from motor import motor_asyncio
from pymongo import MongoClient
from .config import MONGO_URL

app = FastAPI()


@app.get('/api/healthchecker', tags=["Test API"],)
def read_root():
    return {'message': 'API Up!'}

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(MONGO_URL)
    app.database = app.mongodb_client.get_default_database()
    # app.mongodb_client = motor_asyncio.AsyncIOMotorClient(MONGO_URL)
    # app.database = app.mongodb_client.get_default_database()

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

# including the router
app.include_router(user.user)
