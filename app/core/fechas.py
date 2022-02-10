from typing import Optional

import app.core.productos as _productos
from app.models.fechas import FechasResponse


async def consultar(nombre_producto: Optional[str] = None) -> FechasResponse:
    base = await _productos.get_producto_base()

    fechas_abiertas = base.fechas_abiertas
    fechas_cerradas = base.fechas_cerradas

    if nombre_producto is not None:
        producto = await _productos.buscar_por_nombre(nombre_producto)
        fechas_abiertas = [*fechas_abiertas, *producto.fechas_abiertas]
        fechas_cerradas = [*fechas_cerradas, *producto.fechas_cerradas]

    return FechasResponse(
        fechas_abiertas=fechas_abiertas, fechas_cerradas=fechas_cerradas
    )
