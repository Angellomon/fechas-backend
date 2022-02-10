import app.core.fechas as _fechas
from app.models.fechas import FechasResponse
from fastapi import APIRouter
from fastapi_cache.decorator import cache

router = APIRouter(prefix="/fechas")


@router.get("/", response_model=FechasResponse)
@cache(120)
async def consultar_fechas():
    return await _fechas.consultar()


@router.get("/{nombre_producto}", response_model=FechasResponse)
@cache(120)
async def consultar_fecha_producto(nombre_producto: str):
    return await _fechas.consultar(nombre_producto)
