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
import time
from .helpers.utils import dispatcher_telegram_message
from .config import TOKEN_TELEGRAM


class ActionNews(Action):

    def name(self) -> Text:
        return "action_news"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        news_response = tracker.get_slot("response")
        if news_response:
            news = tracker.get_slot("news")
            message_1 = f"Notícias referente a *{news.upper()}*:".replace("_", "-")
            dispatcher_telegram_message(
                input_message=message_1,
                TOKEN_TELEGRAM=TOKEN_TELEGRAM,
                chat_id=tracker.sender_id
            )
            for result in news_response:
                title=result["title"]
                link=f"https://news.google.com/articles/{result['id']}"
                source=result["source"]["title"]
                date=time.strftime("%d-%m-%Y %H:%M:%S", time.struct_time(result["published_parsed"]))
                message_2 = f"*Titulo da Notícia:* {title}\n\n*Fonte:* {source}\n\n*Data:* {date}\n\n*Link:* {link}".replace("_", "-")
                dispatcher_telegram_message(
                    input_message=message_2,
                    TOKEN_TELEGRAM=TOKEN_TELEGRAM,
                    chat_id=tracker.sender_id
                )
            return []
        else:
            return [FollowupAction("action_news_response_none")]
