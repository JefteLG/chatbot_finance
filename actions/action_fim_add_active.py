# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction

class ActionFimAddActive(Action):

    def name(self) -> Text:
        return "action_fim_add_active"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = tracker.get_slot("response")

        if response == "name_active":
            return [FollowupAction("utter_add_active_none_response")]
        elif response == "success":
            dispatcher.utter_message(response="utter_add_active_success")
        elif response == "fail":
            dispatcher.utter_message(response="utter_add_active_fail")
        dispatcher.utter_message(response="utter_menu_ativos")
        return []
