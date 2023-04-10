import uuid
from typing import Optional
from pydantic import BaseModel, Field


class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    notificacao_rastreio: bool = False
    notificacao_relatorio: bool = False
    rastreio: dict = {}

    class Config:
        schema_extra = {
            "example": {
                "notificacao_rastreio": False,
                "notificacao_relatorio": False,
                "rastreio": {
                        "IRDM11" : {
                            "valor" : 2.4,
                            "status" : "acima"
                        },
                        "PETR4" : {
                            "valor" : 31.0,
                            "status" : "abaixo"
                        }
                    }
            }
        }


class UpdateUserTracker(BaseModel):
    rastreio: dict

    class Config:
        schema_extra = {
            "example": {
                "rastreio": {
                        "IRDM11" : {
                            "valor" : 2.4,
                            "status" : "acima"
                        }
                    }
            }
        }


class DeletUserTracker(BaseModel):
    rastreio: str = "IRDM11"


class UpdateUserNotification(BaseModel):
    notificacao_rastreio: Optional[bool]
    notificacao_relatorio: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "notificacao_rastreio": False,
                "notificacao_relatorio": False
            }
        }
