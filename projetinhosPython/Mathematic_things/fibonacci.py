def fibonacci(x) -> list:
    f = [0, 1]
    for i in range(x):
        f.append(f[i] + f[i+1])
    return f


if __name__ == '__main__':
    print(fibonacci(20))
