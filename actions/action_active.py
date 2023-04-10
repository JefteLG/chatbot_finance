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


class ActionActive(Action):

    def name(self) -> Text:
        return "action_active"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        active_response = tracker.get_slot("response")

        if active_response:
            dispatcher.utter_message(response="utter_active_response")
            return []
        else:
            return [FollowupAction("action_active_response_none")]
