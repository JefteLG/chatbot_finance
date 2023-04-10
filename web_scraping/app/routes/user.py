from fastapi import APIRouter, status, Request, Body, HTTPException, Response
from fastapi.encoders import jsonable_encoder
import requests
import logging
from datetime import datetime
from models.User import (
    User, 
    UpdateUserNotification, 
    UpdateUserTracker,
    DeletUserTracker
)
from ..config import YAHOO

user = APIRouter()

# Log Config
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

## Retornar os dados do usuario pelo id
@user.get(
        "/user/{id}", 
        tags=["User"],
        response_description="Get user",
        status_code=status.HTTP_200_OK, 
        response_model=User
    )
def find_one_user(id, request: Request):
    user = request.app.database["users"].find_one({"_id": id})
    return user

## Criar usuarios
@user.post(
        "/user/add/{id}",
        tags=["User"],
        response_description="Create new user",
        status_code=status.HTTP_201_CREATED,
        response_model=User
    )
def create_user(id, request: Request, user: User = Body(...)):
    user = jsonable_encoder(user)
    user.update(_id = id)
    new_user = request.app.database["users"].insert_one(user)
    created_user = request.app.database["users"].find_one(
        {"_id": new_user.inserted_id}
    )
    return created_user

## Adicionar ativos Atualizando os dados do usuario
@user.post(
        "/user/tracker/{id}",
        tags=["User"],
        response_description="create a active the user",
        status_code=status.HTTP_201_CREATED,
        response_model=UpdateUserTracker
    )
def create_user_tracker(id: str, request: Request, user: UpdateUserTracker = Body(...)):
    update_data = {k: v for k, v in user.dict().items() if v is not None}
    response = Response()
    if len(update_data) == 1:
        user = request.app.database["users"].find_one({"_id": id})
        rastreio = user.get("rastreio")
        for key in rastreio.keys():
            if list(update_data.get("rastreio").keys())[0] == key:
                response.status_code = status.HTTP_406_NOT_ACCEPTABLE
                return response

        user.get("rastreio").update(update_data.get("rastreio"))
    
        active = request.app.database["actives"].find_one({"_id": "active"})
        update_data_keys = list(update_data["rastreio"].keys())[0]
        
        response_value = requests.get(
            YAHOO+update_data_keys+".SA?interval=1m",
            headers={"User-Agent": "Mozilla/5.0"}
        )
        if response_value and response_value.status_code == 200:

            active_value = response_value.json()["chart"]["result"][0]["meta"]["regularMarketPrice"]
            if update_data_keys not in list(active.keys()):
                ## Atualiza os valores dos ativos
                active.update({update_data_keys: active_value})
                request.app.database["actives"].update_one(
                    {"_id": "active"}, {"$set": active}
                )
            
            ## Adiciona Ativos no rastreio do usuario
            request.app.database["users"].update_one(
                {"_id": id}, {"$set": user}
            )
            return user
    response.status_code = status.HTTP_404_NOT_FOUND
    return response

## Remove ativos dos usuario
@user.put(
        "/user/remove/tracker/{id}",
        tags=["User"],
        response_description="remove a active the user",
        status_code=status.HTTP_200_OK,
    )
def remove_user_tracker(id: str, request: Request, user: DeletUserTracker):
    update_data = {k: v for k, v in user.dict().items() if v is not None}
    if update_data:
        user = request.app.database["users"].find_one({"_id": id})
        for key in user.get("rastreio").keys():
            if update_data.get("rastreio") == key:
                user.get("rastreio").pop(update_data.get("rastreio").upper())
                request.app.database["users"].update_one(
                    {"_id": id}, {"$set": user}
                )
                return user
    response = Response()
    response.status_code = status.HTTP_404_NOT_FOUND
    return response

## Atualiza as notificações do usuario
@user.put(
        "/user/notification/{id}",
        tags=["User"],
        response_description="Update a notification the user",
        status_code=status.HTTP_200_OK,
        response_model=UpdateUserNotification
    )
def update_user_notification(id: str, request: Request, user: UpdateUserNotification = Body(...)):
    update_data = {k: v for k, v in user.dict().items() if v is not None}
    if len(update_data) >= 1:
        user = request.app.database["users"].find_one({"_id": id})
        user.update(update_data)
        request.app.database["users"].update_one(
            {"_id": id}, {"$set": user}
        )
    if (exist_user := request.app.database["users"].find_one({"_id": id})) is not None:
        return exist_user
    return "User not found"

## Atualiza os valores das ações 
@user.put(
        "/active/update",
        tags=["Active"],
        response_description="Update all actives",
        status_code=status.HTTP_200_OK
    )
def update_actives(request: Request):
    active_data = request.app.database["actives"].find_one({"_id": "active"})
    actives_dict = {}
    for active in active_data.keys():
        if active == "_id":
            continue
        response_value = requests.get(
            YAHOO+active+".SA?interval=1m",
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
            }
        )
        logger.info(f"Tempo: {datetime.now().strftime('%H:%M:%S')}")
        if response_value and response_value.status_code == 200:
            active_value = response_value.json()["chart"]["result"][0]["meta"]["regularMarketPrice"]
            actives_dict[active] = active_value
    active_data.update(actives_dict)
    request.app.database["actives"].update_one(
        {"_id": "active"}, {"$set": active_data}
    )
    return active_data
