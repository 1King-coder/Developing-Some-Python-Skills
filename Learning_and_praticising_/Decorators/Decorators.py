import datetime


def log(func):
    def wrapper():
        with open("./log.txt", 'a') as log:
            if 'class' in str(type(func)):
                log.writelines(
                    f'Class {func.__name__} initialized at '
                    f'{datetime.datetime.now()} \n'
                )

            log.writelines(
                f'Function {func.__name__} was called at '
                f'{datetime.datetime.now()} \n'
            )

        return func

    return wrapper()


@log
def random_func(value_1, value_2):
    print(value_2 + value_1)


@log
class SomeClass:
    def __init__(self, id):
        self.id = id

    def show_id(self):
        print(self.id)


random_func(2, 1)

class_ = SomeClass(1101)

class_.show_id()
