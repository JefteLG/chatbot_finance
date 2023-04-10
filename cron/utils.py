import requests
import urllib.parse
import logging
from datetime import datetime

# Função para entrega de mensagens no telegram de forma personalizada
def dispatcher_telegram_message(input_message, chat_id, TOKEN_TELEGRAM):
    text = {"text": f"{input_message}"}
    response = requests.post(
        f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&{urllib.parse.urlencode(text)}"
    )
    logging.info(f"Endpoint: {response.url}")
    logging.info(f"Status da requisição {response.status_code}")
    logging.info(f"Tempo: {datetime.now().strftime('%H:%M:%S.%f')}")
    logging.info("==================================================================================")
    return response.status_code