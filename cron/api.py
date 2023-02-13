#!/usr/bin/env python
import requests
import logging
import traceback
from datetime import datetime

# Log Config
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    r = requests.get("http://192.168.1.69:5000")
    logger.info(f"Status da requisição {r.status_code}")
    logger.info(f"conteudo da requisição {r.content}")
    logger.info(f"Tempo: {datetime.now().strftime('%H:%M:%S')}")
except Exception:
    traceback.print_exc()
