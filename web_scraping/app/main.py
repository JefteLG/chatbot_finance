from fastapi import FastAPI
from .routes import user
from dotenv import dotenv_values
# from motor import motor_asyncio
from pymongo import MongoClient

config = dotenv_values(".env")
app = FastAPI()


@app.get('/api/healthchecker', tags=["Test API"],)
def read_root():
    return {'message': 'API Up!'}

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGO_URL"])
    app.database = app.mongodb_client.get_default_database()
    print(f"AAAAAAAAAAA --- {app.database}")
    # app.mongodb_client = motor_asyncio.AsyncIOMotorClient(config["MONGO_URL"])
    # app.database = app.mongodb_client.get_default_database()

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

# including the router
app.include_router(user.user)
