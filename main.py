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

    print("\n========== SISTEMA INTEGRAL SOFTWARE FJ ==========\n")

    print("\n----- REGISTRO DE CLIENTES -----")

    cliente1 = sistema.registrar_cliente(
        "Luis Felipe Suárez Muñoz",
        "lfsuarezmu@unadvirtual.edu.co",
        "1017146556"
    )

    cliente2 = sistema.registrar_cliente(
        "Juan David Rivera Betancur",
        "jdriverabetancur27@unadvirtual.edu.co",
        "87654321"
    )

    cliente3 = sistema.registrar_cliente(
        "Luis Mariano Bedoya Velásquez",
        "luismaribedoya22@unadvirtual.edu.co",
        "11223344"
    )

    cliente4 = sistema.registrar_cliente(
        "Daniela Castro Chaverra",
        "danielacastrocha1@gmail.com",
        "12345678"
    )

    # Casos inválidos (para probar excepciones)
    sistema.registrar_cliente("", "correo@gmail.com", "123456")
    sistema.registrar_cliente("Cliente Sin Correo", "correo_invalido", "123456")
    sistema.registrar_cliente("Cliente Documento Malo", "cliente@gmail.com", "ABC123")

    print("\n----- CREACIÓN DE SERVICIOS -----")

    sala = Sala("Sala VIP", 50000)
    equipo = Equipo("Laptop Dell", 30000)
    asesoria = Asesoria("Consultoría en software", 100000)
    servicio_no_disponible = Sala("Sala de Conferencias", 80000, disponible=False)

    sistema.agregar_servicio(sala)
    sistema.agregar_servicio(equipo)
    sistema.agregar_servicio(asesoria)
    sistema.agregar_servicio(servicio_no_disponible)

    print("\n----- CREACIÓN DE RESERVAS -----")

    sistema.crear_reserva(cliente1, sala, 2)
    sistema.crear_reserva(cliente2, equipo, 3, impuesto=0.19)
    sistema.crear_reserva(cliente3, asesoria, 1, impuesto=0.19, descuento=20000)

    # Reserva adicional
    sistema.crear_reserva(cliente4, sala, 3, impuesto=0.19)

    # Casos con error
    sistema.crear_reserva(cliente1, sala, -1)
    sistema.crear_reserva(cliente2, equipo, 0)
    sistema.crear_reserva(cliente3, servicio_no_disponible, 2)

    print("\n=== RESUMEN ===")
    print(f"Clientes registrados: {len(sistema.clientes)}")
    print(f"Servicios registrados: {len(sistema.servicios)}")
    print(f"Reservas exitosas: {len(sistema.reservas)}")


if __name__ == "__main__":
    ejecutar_simulacion()