# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .helpers.mongo import connect_mongodb
import requests
import logging

# Log Config
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class ActionGreetInit(Action):

    def name(self) -> Text:
        return "action_greet_init"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        client = connect_mongodb() 
        db = client.get_default_database()
        collection = db.users
        user = tracker.sender_id 
        users_id = collection.find().distinct("_id")

        if user not in users_id:
            url = f"http://web_scraping/user/add/{user}"
            data = {
                "notificacao_rastreio": True,
                "notificacao_relatorio": False,
                "rastreio": {}
            }
            create_user = requests.post(url, json=data)

            if create_user and create_user.status_code == 201:
                logging.info("Usuario Cadastrado")
            else:
                logging.info("Usuario não cadastrado")

        dispatcher.utter_message(response="utter_saudar_1")
        dispatcher.utter_message(response="utter_saudar_2")

        return []
