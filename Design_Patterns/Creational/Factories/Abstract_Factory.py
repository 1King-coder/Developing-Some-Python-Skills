
"""
Abstract Factory é um padrão de criação que fornece uma interface para criar
famílias de objetos relacionados ou dependentes sem especificar suas classes
concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods
para criar seus objetos.
Uma diferença importante entre Factory Method e Abstract Factory é que o
Factory Method usa herança, enquanto Abstract Factory usa a composição.
Princípio: programe para interfaces, não para implementações
"""


from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZN a caminho do cliente . . .')


class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZS a caminho do cliente . . .')


class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular ZN a caminho do cliente . . .')


class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular ZS a caminho do cliente . . .')


class CombeZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Combe a ZN caminho do cliente . . .')


class CombeZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Combe a ZS caminho do cliente . . .')


class MotoPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto popular a ZN caminho do cliente . . .')


class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto popular a ZS caminho do cliente . . .')


class MotoLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZN a caminho do cliente . . .')


class MotoLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZS a caminho do cliente . . .')


class LimousineZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Limousine a ZN caminho do cliente . . .')


class LimousineZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Limousine a ZS caminho do cliente . . .')


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo: pass
    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular: pass
    @staticmethod
    @abstractmethod
    def get_moto_luxo() -> VeiculoLuxo: pass
    @staticmethod
    @abstractmethod
    def get_moto_popular() -> VeiculoPopular: pass
    @staticmethod
    @abstractmethod
    def get_combe() -> VeiculoPopular: pass
    @staticmethod
    @abstractmethod
    def get_limousine() -> VeiculoLuxo: pass


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZN()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZN()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZN()

    @staticmethod
    def get_combe() -> VeiculoPopular:
        return CombeZN()

    @staticmethod
    def get_limousine() -> VeiculoLuxo:
        return LimousineZN()


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZS()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZS()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZS()

    @staticmethod
    def get_combe() -> VeiculoPopular:
        return CombeZS()

    @staticmethod
    def get_limousine() -> VeiculoLuxo:
        return LimousineZS()


class Cliente:
    def buscar_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente()

            combe = factory.get_combe()
            combe.buscar_cliente()

            limousine = factory.get_limousine()
            limousine.buscar_cliente()


if __name__ == '__main__':
    cliente = Cliente()
    cliente.buscar_clientes()
