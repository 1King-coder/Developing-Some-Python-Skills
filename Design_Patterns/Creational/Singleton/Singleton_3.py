class Meta(type):
    def __call__(cls, *args, **kwargs):
        print('Método CALL da METACLASS é chamado 1º')
        return super().__call__(*args, **kwargs)


class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('NEW é executado 1º')
        return super().__new__(cls)

    def __init__(self, nome):
        print('INIT é executado 2º')
        self.nome = nome
        self.status = None

    def __call__(self, order=None):
        print('Método CALL da ORIGINALCLASS é chamado 2º')
        if not self.status:
            print('Pessoa Desempregada')
        else:
            print(f'Pessoa {self.status}')
        if order == 'empregar':
            self.status = 'empregada'
            print('Pessoa Contratada')
        if order == 'demitir':
            self.status = None
            print('Pessoa Demitida')


p1 = Pessoa('Luiz')
p1()
