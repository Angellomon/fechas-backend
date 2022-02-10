import app.core.productos as _productos
from app.models.productos import Producto, ProductoCreate, ProductoDB, ProductoUpdate
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException

router = APIRouter(prefix="/productos")


@router.post("/", response_model=Producto)
async def crear_producto(producto_data: ProductoCreate):
    try:
        producto = await _productos.crear(producto_data)
    except AssertionError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{err}")

    return producto


@router.patch("/", response_model=Producto)
async def update_base(producto_data: ProductoUpdate):
    return await _productos.update("__base__", producto_data)


@router.get("/{nombre}", response_model=Producto)
async def get_producto(nombre: str):
    return await _productos.buscar_por_nombre(nombre)


@router.patch("/{nombre}", response_model=Producto)
async def update_producto(nombre: str, producto_data: ProductoUpdate):
    return await _productos.update(nombre, producto_data)


@router.delete("/{nombre}", response_model=Producto)
async def delete_producto(nombre: str):
    try:
        return await _productos.delete(nombre)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{err}")
