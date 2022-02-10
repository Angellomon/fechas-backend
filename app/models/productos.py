from app.models.utils import ConFechas, DBModel


class _ProductoBase(ConFechas):
    nombre: str


class ProductoUpdate(ConFechas):
    ...


class ProductoCreate(_ProductoBase):
    ...


class Producto(_ProductoBase):
    ...


class ProductoDB(Producto, DBModel):
    class Collection:
        indexes = ["nombre"]
