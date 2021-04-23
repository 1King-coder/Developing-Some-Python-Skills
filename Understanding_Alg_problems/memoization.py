"""
def f(n):
    if n <= 2:
        return 1
    return f(n - 1) + f(n - 2)
"""


def f(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = f(n - 1) + f(n - 2)
    return memo[n]


print(f(994))
