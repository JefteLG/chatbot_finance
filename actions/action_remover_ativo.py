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
from rasa_sdk.events import FollowupAction


class ActionRemoverAtivo(Action):

    def name(self) -> Text:
        return "action_remover_ativo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        client = connect_mongodb() 
        db = client.get_default_database()
        user = tracker.sender_id

        user_data = db["users"].find_one({"_id": user}).get("rastreio")

        if user_data:
            dispatcher.utter_message(response="utter_remover_ativo_sim_1")
            for key in user_data.keys():
                dispatcher.utter_message(text=f"{key.upper()}")
        else:
            return [FollowupAction("utter_remove_active_none_active")]
