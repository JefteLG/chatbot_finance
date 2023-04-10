from typing import Any, Text, Dict, List
import traceback
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from .helpers.pygooglenews import GoogleNews


class ValidateNewsForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_news_form"

    def validate_news(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        """
        Validate news
        """
        if tracker.get_slot("news"):
            try:
                gn = GoogleNews(lang='pt', country='BR')
                search_results = gn.search(slot_value, when='14d')
                top_results = search_results['entries'][:3]
                if top_results:
                    return {"news": slot_value.upper(), "response": top_results}
                else:
                    return {"news": slot_value.upper(), "response": None}
            except Exception:
                traceback.print_exc()
                return {"news": slot_value.upper(), "response": None}
        return {"news": slot_value, "response": None}
