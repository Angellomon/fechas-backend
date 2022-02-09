from app.models.productos import Producto


def get_default_producto():
    return Producto(
        nombre="__base__",
    )
