from app.core.errors import EntityNotFound
from app.models.productos import Producto, ProductoCreate, ProductoDB, ProductoUpdate
from loguru import logger


async def get_producto_base():
    producto_db = await ProductoDB.find_one(ProductoDB.nombre == "__base__")

    if producto_db is None:
        raise EntityNotFound("producto-base", "no hay un producto base configurado")

    return Producto(**producto_db.dict())


async def buscar_por_nombre(nombre: str):
    producto = await ProductoDB.find_one(ProductoDB.nombre == nombre)

    if producto is None:
        raise EntityNotFound(
            "producto", f"no se ha encontrado el producto (nombre={nombre})"
        )

    return producto


async def crear(producto_data: ProductoCreate):
    assert producto_data.nombre != "__base__", "no se puede"

    is_none = (
        await ProductoDB.find_one(ProductoDB.nombre == producto_data.nombre)
    ) is None

    assert is_none, f"el producto ya existe (nombre{producto_data.nombre})"

    producto_db = ProductoDB(**producto_data.dict())

    await producto_db.insert()

    return Producto(**producto_db.dict())


async def update(nombre_producto: str, producto_data: ProductoUpdate):
    producto_db = await buscar_por_nombre(nombre_producto)

    producto_db.fechas_abiertas = (
        producto_data.fechas_abiertas or producto_db.fechas_abiertas
    )
    producto_db.fechas_cerradas = (
        producto_data.fechas_cerradas or producto_db.fechas_cerradas
    )

    await producto_db.save()

    return Producto(**producto_db.dict())


async def delete(nombre_producto: str):
    if nombre_producto == "__base__":
        raise ValueError("no se puede")

    producto_db = await buscar_por_nombre(nombre_producto)

    logger.debug(f"eliminado: {producto_db.dict()}")

    await producto_db.delete()

    return Producto(**producto_db.dict())
