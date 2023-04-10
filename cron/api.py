#!/usr/bin/env python
import logging
import traceback
from pymongo import MongoClient
from utils import dispatcher_telegram_message
from config import TOKEN_TELEGRAM, MONGO_URL

# Log Config
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    mongodb_client = MongoClient(MONGO_URL)
    database = mongodb_client.get_default_database()
    users_id = database["users"].find().distinct("_id")
    active_data = database["actives"].find_one({"_id": "active"})

    for user in users_id:
        user_data = database["users"].find_one({"_id": user})
        if user_data.get("notificacao_rastreio") and user_data.get("rastreio"):
            for key, value in user_data.get("rastreio").items():
                active_value = active_data.get(key)
                if active_value is None:
                    continue
                status = value["status"]
                user_active_value = value["valor"]
                if (status == "abaixo" and active_value < user_active_value) \
                    or \
                    (status == "acima" and active_value > user_active_value):
                    message = f"O Ativo *{key}* está no valor *R$ {active_value}*."
                    dispatcher_telegram_message(
                        input_message=message,
                        TOKEN_TELEGRAM=TOKEN_TELEGRAM,
                        chat_id=user
                    )
except Exception:
    traceback.print_exc()
