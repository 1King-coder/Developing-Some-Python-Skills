"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""


from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo a caminho do cliente . . .')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular a caminho do cliente . . .')


class Combe(Veiculo):
    def buscar_cliente(self) -> None:
        print('Combe a caminho do cliente . . .')


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto popular a caminho do cliente . . .')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo a caminho do cliente . . .')


class Limousine(Veiculo):
    def buscar_cliente(self) -> None:
        print('Limousine a caminho do cliente . . .')


class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'combe':
            return Combe()
        if tipo == 'moto_luxo':
            return MotoLuxo()
        if tipo == 'moto_popular':
            return MotoPopular()
        if tipo == 'limousine':
            return Limousine()
        assert 0, 'Veículo inexistente'


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'combe':
            return Combe()
        if tipo == 'moto_popular':
            return MotoPopular()
        assert 0, 'Veículo inexistente'


if __name__ == '__main__':
    from random import choice

    veiculos_disponiveis_zona_norte = [
        'luxo', 'popular', 'combe', 'moto_luxo', 'moto_popular', 'limousine']
    veiculos_disponiveis_zona_sul = ['popular', 'combe', 'moto_popular']

    print('ZONA NORTE')
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(
            choice(veiculos_disponiveis_zona_norte))
        carro.buscar_cliente()

    print()

    print('ZONA SUL')
    for i in range(10):
        carro = ZonaSulVeiculoFactory(
            choice(veiculos_disponiveis_zona_sul))
        carro.buscar_cliente()
