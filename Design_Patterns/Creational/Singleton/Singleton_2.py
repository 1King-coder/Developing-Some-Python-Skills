def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]

    return get_class


@singleton
class AppSettings:
    def __init__(self):
        self.tema = 'Tema Escuro'


@singleton
class Teste:
    def __init__(self):
        print('Olá Mundo')


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'Tema Claro'
    print(as1.tema)

    as2 = AppSettings()
    print(as1.tema)

    print(as1)
    print(as2)
    print(as1 == as2)
    print(id(as1) == id(as2))

    t1 = Teste()
    t2 = Teste()
    print(t1 == t2)
