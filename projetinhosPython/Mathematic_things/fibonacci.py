

def fibonacci(u):
    f = [0, 1]
    for i in range(u):
        f.append(f[i] + f[i+1])
    return f


print(fibonacci(100))
