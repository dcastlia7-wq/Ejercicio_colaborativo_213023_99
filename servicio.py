from abc import ABC, abstractmethod
from cliente import ValidacionError, SistemaError

class ServicioError(SistemaError):
    pass


class Servicio(ABC):
    def __init__(self, nombre, costo_base, disponible=True):
        self.nombre = nombre
        self.costo_base = costo_base
        self.disponible = disponible
        self.validar_servicio()

    def validar_servicio(self):
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ServicioError("El nombre del servicio no puede estar vacío.")

        if not isinstance(self.costo_base, (int, float)) or self.costo_base <= 0:
            raise ServicioError("El costo base del servicio debe ser mayor que cero.")

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    def validar_disponibilidad(self):
        if not self.disponible:
            raise ServicioError(f"El servicio '{self.nombre}' no se encuentra disponible.")


class Sala(Servicio):
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        if duracion <= 0:
            raise ValidacionError("Horas inválidas")
        subtotal = self.costo_base * duracion
        return subtotal + (subtotal * impuesto) - descuento

    def descripcion(self):
        return f"Reserva de sala: {self.nombre}"


class Equipo(Servicio):
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        if duracion <= 0:
            raise ValidacionError("Días inválidos")
        subtotal = self.costo_base * duracion
        return subtotal + (subtotal * impuesto) - descuento

    def descripcion(self):
        return f"Alquiler de equipo: {self.nombre}"


class Asesoria(Servicio):
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        if duracion <= 0:
            raise ValidacionError("Horas inválidas")
        subtotal = self.costo_base * duracion
        return subtotal + (subtotal * impuesto) - descuento

    def descripcion(self):
        return f"Asesoría especializada: {self.nombre}"