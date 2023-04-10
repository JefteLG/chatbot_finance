# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from .helpers.mongo import connect_mongodb
# from .helpers.utils import dispatcher_telegram_message
# from .config import TOKEN_TELEGRAM

# class ActionVerifyActive(Action):

#     def name(self) -> Text:
#         return "action_verify_active"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         client = connect_mongodb() 
#         db = client.get_default_database()
#         user = tracker.sender_id

#         user_data = db["users"].find_one({"_id": user}).get("rastreio")
#         if user_data:
#             active_data = db["actives"].find_one({"_id": "active"})

#             for key, value in user_data.items():
#                 active_value = active_data.get(key)
#                 if active_value is None:
#                     continue

#                 status = value["status"]
#                 user_active_value = value["valor"]

#                 if (status == "abaixo" and active_value < user_active_value) \
#                     or \
#                     (status == "acima" and active_value > user_active_value):
#                     message = f"O Ativo *{key}* está no valor *R$ {active_value}*."
#                     dispatcher_telegram_message(
#                         input_message=message,
#                         TOKEN_TELEGRAM=TOKEN_TELEGRAM,
#                         chat_id=user
#                     )
#         return []
