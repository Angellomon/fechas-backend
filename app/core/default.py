from app.models.productos import Producto, ProductoDB

_default_nombre = "__base__"


def get_default_producto():
    return ProductoDB(
        nombre=_default_nombre,
    )


async def initial_setup():
    producto_base = await ProductoDB.find_one(ProductoDB.nombre == _default_nombre)

    if producto_base is None:
        producto_base = get_default_producto()

        await producto_base.insert()
