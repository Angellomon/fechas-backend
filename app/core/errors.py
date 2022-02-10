from fastapi import status
from fastapi.exceptions import HTTPException


class EntityNotFound(HTTPException):
    def __init__(self, entidad: str, mensaje: str = "") -> None:
        super().__init__(
            status.HTTP_404_NOT_FOUND,
            f"entidad no encontrada (entidad={entidad}, mensaje: {mensaje})",
        )
