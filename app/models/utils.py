from datetime import date, datetime
from typing import Any, List, Union

from beanie import Document
from pydantic.class_validators import validator
from pydantic.fields import Field
from pydantic.main import BaseModel

default_now = Field(default_factory=lambda: datetime.now())

default_nombre = "__base__"


def parse_fecha(fecha: Union[str, datetime, date]):
    if isinstance(fecha, (datetime, date)):
        return fecha

    try:
        return datetime.strptime(fecha, "%Y-%m-%d")
    except:
        return datetime.fromisoformat(fecha)


class ConFechas(BaseModel):
    fechas_abiertas: List[datetime] = []
    fechas_cerradas: List[datetime] = []

    @validator("fechas_abiertas", "fechas_cerradas", pre=True)
    def validar_fechas(cls, value: Any):
        return [parse_fecha(fecha) for fecha in value]


class DBModel(Document):
    created_at: datetime = default_now
    updated_at: datetime = default_now
