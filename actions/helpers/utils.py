import requests
import urllib.parse

# Função para entrega de mensagens no telegram de forma personalizada
def dispatcher_telegram_message(input_message, chat_id, TOKEN_TELEGRAM):
    text = {"text": f"{input_message}"}
    response = requests.post(
        f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&{urllib.parse.urlencode(text)}"
    )
    return response.status_code
