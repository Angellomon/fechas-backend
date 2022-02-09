from app.models.utils import ConFechasAbiertas, ConFechasCerradas, DBModel


class Producto(DBModel, ConFechasAbiertas, ConFechasCerradas):

    nombre: str
