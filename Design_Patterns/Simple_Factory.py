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


class VeiculoFactory:
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'combe':
            return Combe()
        assert 0, 'Veículo inexistente'

    def buscar_cliente(self):
        self.carro.buscar_cliente()


if __name__ == '__main__':
    from random import choice

    carros_disponiveis = ['luxo', 'popular', 'combe']

    for i in range(10):
        carro = VeiculoFactory(choice(carros_disponiveis))
        carro.buscar_cliente()
