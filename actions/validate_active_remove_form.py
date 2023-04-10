from typing import Any, Text, Dict, List
import traceback
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import requests

class ValidateRemoveActiveForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_remove_active_form"

    def validate_remove_active(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        """
        Validate remove active
        """

        if tracker.get_slot("remove_active"):
            try:
                api = f"http://web_scraping:80/user/remove/tracker/{tracker.sender_id}"
                update_notification = requests.put(api, json={"rastreio": slot_value.upper()})
                if update_notification and update_notification.status_code == 200:
                    return {"remove_active": slot_value.upper(), "response": "Atualizado"}
                else:
                    return {"remove_active": slot_value.upper(), "response": None}
            except Exception:
                traceback.print_exc()
                return {"remove_active": slot_value.upper(), "response": None}
        return {"remove_active": slot_value, "response": None}
