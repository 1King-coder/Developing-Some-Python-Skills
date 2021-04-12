class StrReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__} ({params})'

    def __repr__(self):
        return self.__str__()


class A(StrReprMixin):
    def __init__(self, nome):
        self.x = 10
        self.y = 20
        self.nome = nome


class MonoState(StrReprMixin):
    _state: dict = {
        'x': 200,
        'y': 900,
        'nome': 'Vitor'
    }

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self, nome=None):
        if nome is not None:
            self.nome = nome


class B(MonoState):
    pass


if __name__ == '__main__':
    m1 = MonoState('Vitor')
    print(m1)

    m2 = MonoState()
    print(m1)

    b = B()
    print(b)
