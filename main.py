import logging
from sistema import SistemaGestion
from servicio import Sala, Equipo, Asesoria

logging.basicConfig(
    filename="sistema_gestion.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def ejecutar_simulacion():
    sistema = SistemaGestion()

    cliente = sistema.registrar_cliente("Laura", "laura@gmail.com", "12345678")

    sala = Sala("VIP", 50000)
    sistema.agregar_servicio(sala)

    reserva, costo = sistema.crear_reserva(cliente, sala, 2)

    print(reserva.mostrar_info())
    print("Costo:", costo)


if __name__ == "__main__":
    ejecutar_simulacion()