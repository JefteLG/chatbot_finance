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

class ActionFimRemoverAtivo(Action):

    def name(self) -> Text:
        return "action_fim_remover_ativo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        remove_active_response = tracker.get_slot("response")

        if remove_active_response:
            dispatcher.utter_message(response="utter_remove_active_response")
            return []
        else:
            return [FollowupAction("utter_remove_active_none_response")]
