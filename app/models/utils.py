from datetime import datetime
from typing import List

import nanoid
from beanie import Document
from pydantic import BaseModel
from pydantic.fields import Field

default_now = Field(default_factory=lambda: datetime.now())


class ConFechasAbiertas:
    fechas_abiertas: List[datetime] = []


class ConFechasCerradas:
    fechas_cerradas: List[datetime] = []


class DBModel(Document):
    id: str = Field(default_factory=lambda: nanoid())

    created_at: datetime = default_now
    updated_at: datetime = default_now
