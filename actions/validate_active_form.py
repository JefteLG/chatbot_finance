from typing import Any, Text, Dict, List
import traceback
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from .config import YAHOO
import requests

class ValidateActiveForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_active_form"

    def validate_active(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        """
        Validate active
        """
        if tracker.get_slot("active"):
            try:
                response_value = requests.get(
                    YAHOO+slot_value+".SA?interval=1m",
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Connection': 'keep-alive',
                    }
                )
                if response_value and response_value.status_code == 200:
                    active_value = response_value.json()["chart"]["result"][0]["meta"]["regularMarketPrice"]
                    return {"active": slot_value.upper(), "response": active_value}
                else:
                    return {"active": slot_value.upper(), "response": None}
            except Exception:
                traceback.print_exc()
                return {"active": slot_value.upper(), "response": None}
        return {"active": slot_value, "response": None}
