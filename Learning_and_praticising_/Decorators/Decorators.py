import datetime


def log(func):
    def wrapper():
        with open("./log.txt", 'a') as log:
            log.writeline(
                f'Function {func.__name__} was called at '
                f'{datetime.datetime.now()}'
            )
        return func

    return wrapper()


@log
def random_func(value_1, value_2):
    print(value_2 + value_1)


random_func(2, 1)
