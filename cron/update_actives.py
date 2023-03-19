#!/usr/bin/env python
import requests
import logging
import traceback
from dotenv import dotenv_values
from pymongo import MongoClient
from datetime import datetime

config = dotenv_values(".env")

# Log Config
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    string_connection = "mongodb://user:tst123@mongodb:27017/bot_invest?authSource=admin"
    mongodb_client = MongoClient(string_connection)
    database = mongodb_client.get_default_database()
    collection = database.actives
    active_data = collection.find_one({"_id": "active"})

    if active_data:
        api = "http://web_scraping:80/active/update"
        response_value = requests.put(api)
        logger.info(f"Endpoint: {response_value.url}")
        logger.info(f"Status da requisição {response_value.status_code}")
        logger.info(f"Tempo: {datetime.now().strftime('%H:%M:%S.%f')}")
        logger.info("==================================================================================")

except Exception:
    traceback.print_exc()
