from fastapi import APIRouter

from .endpoints.fechas import router as _fechas_router
from .endpoints.productos import router as _productos_router

router = APIRouter()

router.include_router(_productos_router)
router.include_router(_fechas_router)
