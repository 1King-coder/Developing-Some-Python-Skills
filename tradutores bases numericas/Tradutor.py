import re


def bin_to_deci(x):
    x = str(x)
    soma = 0
    length = len(x) - 1
    for i in x:
        soma += int(i)*2**length
        length -= 1
    return soma


def deci_to_bin(x):
    x = int(x)
    string_bin = ''
    while x//2 != 0:
        string_bin += str(x % 2)
        x = x//2
    string_bin += str(x % 2)
    return f'{string_bin[::-1]:0>8}'
