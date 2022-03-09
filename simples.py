import sympy

def resolve_simples(data):
    tamanholista = len(data)
    primos = 0
    for i in range(tamanholista):
        if sympy.isprime(data[i]):
            primos += 1
    return primos