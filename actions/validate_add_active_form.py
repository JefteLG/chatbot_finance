from typing import Any, Text, Dict, List
import traceback
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import requests
from .config import YAHOO

class ValidateAddActiveForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_add_active_form"

    def validate_name_active(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        """
        Validate name active
        """

        if tracker.get_slot("name_active"):
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
                    return {
                        "name_active": slot_value.upper(),
                        "value_active_pregao": active_value,
                        "response": None
                    }
                else:
                    return {"name_active": slot_value.upper(), "response": "name_active", "requested_slot": None}
            except Exception:
                traceback.print_exc()
                return {"name_active": slot_value.upper(), "response": "name_active", "requested_slot": None}
        return {"name_active": slot_value, "response": None}
 
    def validate_value_active(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        """
        Validate value active
        """

        if tracker.get_slot("value_active"):
            try:
                if str(slot_value).lower() == "sair":
                    return {"requested_slot": None, "response": "sair"}
                value_active = float(str(tracker.get_slot("value_active")).replace(",", "."))
                name_active = tracker.get_slot("name_active")
                value_active_pregao = tracker.get_slot("value_active_pregao")
                status = "acima" if value_active >= value_active_pregao else "abaixo"
                api = f"http://web_scraping:80/user/tracker/{tracker.sender_id}"
                data = {
                    "rastreio": {
                        f"{name_active}": {
                        "valor": value_active,
                        "status": status
                        }
                    }
                }
                add_active = requests.post(api, json=data)
                if add_active and add_active.status_code in [200, 201]:
                    return {"value_active": value_active, "response": "success"}
                else:
                    return {"value_active": value_active, "response": "fail"}
            except Exception:
                traceback.print_exc()
                return {"value_active": None, "response": "value_active"}
        return {"value_active": slot_value, "response": None}
