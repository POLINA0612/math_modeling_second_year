def add(n):
    def decorator(func):
        def wrapper(x):
            return func(x + n)
        return wrapper
    return decorator

@add(5)
def f(x):
    return x

print(f(15))