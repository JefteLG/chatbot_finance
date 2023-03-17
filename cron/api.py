#!/usr/bin/env python
import requests
import logging
import traceback
from datetime import datetime
from dotenv import dotenv_values
from pymongo import MongoClient

config = dotenv_values(".env")

# Log Config
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    string_connection = "mongodb://user:tst123@mongodb:27017/bot_invest?authSource=admin"
    mongodb_client = MongoClient(string_connection)
    database = mongodb_client.get_default_database()
    collection = database.users
    users_id = collection.find().distinct("_id")

    for user in users_id:
        data = {"name": "rastreio"}
        r = requests.post(
            f"http://rasa:5005/conversations/{user}/trigger_intent",
            json=data)
        logger.info(f"Endpoint: {r.url}")
        logger.info(f"Status da requisição {r.status_code}")
        logger.info(f"conteudo da requisição {r.content}")
        logger.info(f"Tempo: {datetime.now().strftime('%H:%M:%S')}")
except Exception:
    traceback.print_exc()
