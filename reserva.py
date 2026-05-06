import logging
from datetime import datetime
from cliente import Cliente, SistemaError
from servicio import Servicio

class ReservaError(SistemaError):
    pass


class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.fecha_creacion = datetime.now()

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self, impuesto=0, descuento=0):
        try:
            if not isinstance(self.cliente, Cliente):
                raise ReservaError("Cliente inválido")

            if not isinstance(self.servicio, Servicio):
                raise ReservaError("Servicio inválido")

            self.servicio.validar_disponibilidad()
            costo = self.servicio.calcular_costo(self.duracion, impuesto, descuento)

        except Exception as e:
            logging.error(str(e))
            raise ReservaError("Error al procesar reserva") from e

        else:
            self.confirmar()
            return costo

    def mostrar_info(self):
        return f"{self.cliente.mostrar_info()} | {self.servicio.descripcion()} | Estado: {self.estado}"