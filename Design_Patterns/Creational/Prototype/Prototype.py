from __future__ import annotations
from copy import deepcopy


class StrReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__} ({params})'

    def __repr__(self):
        return self.__str__()


class Person(StrReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: list = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


class Address(StrReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == '__main__':
    vitor = Person('Vitor', 'dos Santos Barcelos')
    vitor_address = Address('Nova Iguaçu', '1274')

    vitor.add_address(vitor_address)

    lessa = vitor.clone()
    lessa.firstname = 'Maria Eduarda Lessa Ferreira'

    print(vitor)
    print(lessa)
