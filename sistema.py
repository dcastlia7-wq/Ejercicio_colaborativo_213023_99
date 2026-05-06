import logging
from cliente import Cliente, ValidacionError
from servicio import Servicio
from reserva import Reserva, ReservaError

class SistemaGestion:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, nombre, email, documento):
        try:
            cliente = Cliente(nombre, email, documento)
            self.clientes.append(cliente)
            return cliente

        except ValidacionError as e:
            logging.error(str(e))
            print(e)

    def agregar_servicio(self, servicio):
        if isinstance(servicio, Servicio):
            self.servicios.append(servicio)

    def crear_reserva(self, cliente, servicio, duracion, impuesto=0, descuento=0):
        try:
            reserva = Reserva(cliente, servicio, duracion)
            costo = reserva.procesar(impuesto, descuento)
            self.reservas.append(reserva)
            return reserva, costo

        except ReservaError as e:
            logging.error(str(e))
            print(e)