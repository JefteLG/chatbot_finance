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


class ActionManageNotification(Action):

    def name(self) -> Text:
        return "action_manage_notification"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        client = connect_mongodb()
        db = client.get_default_database()
        user = tracker.sender_id
        user_data = db["users"].find_one({"_id": user}).get("notificacao_rastreio")

        if user_data:
            dispatcher.utter_message(response="utter_ativo_ativados_0")
            return [FollowupAction("utter_ativo_ativados")]
        else:
            return [FollowupAction("action_disabled")]
