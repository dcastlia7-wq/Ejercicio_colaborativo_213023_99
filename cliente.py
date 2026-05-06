from abc import ABC, abstractmethod
import logging

class SistemaError(Exception):
    pass

class ValidacionError(SistemaError):
    pass

class Entidad(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass


class Cliente(Entidad):
    def __init__(self, nombre, email, documento):
        self.__nombre = nombre
        self.__email = email
        self.__documento = documento
        self.validar()
        logging.info(f"Cliente creado correctamente: {self.__nombre}")

    def validar(self):
        if not isinstance(self.__nombre, str) or not self.__nombre.strip():
            raise ValidacionError("El nombre del cliente no puede estar vacío.")

        if not isinstance(self.__email, str) or "@" not in self.__email or "." not in self.__email:
            raise ValidacionError("El correo electrónico no es válido.")

        if not str(self.__documento).isdigit() or len(str(self.__documento)) < 6:
            raise ValidacionError("El documento debe ser numérico y tener mínimo 6 dígitos.")

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} | Email: {self.__email} | Documento: {self.__documento}"