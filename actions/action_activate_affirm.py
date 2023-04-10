# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionActivateAffirm(Action):

    def name(self) -> Text:
        return "action_activate_affirm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:
            user = tracker.sender_id        
            api = f"http://web_scraping:80/user/notification/{user}"
            update_notification = requests.put(api, json={"notificacao_rastreio": False})
            if update_notification and update_notification.status_code == 200:
                dispatcher.utter_message(response="utter_activate_affirm")
            else:
                dispatcher.utter_message(response="utter_activate_affirm_error")
        except Exception:
            dispatcher.utter_message(response="utter_activate_affirm_error")

        return []
