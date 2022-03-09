import sympy
import concurrent.futures


def tCalculaPrimo(data):
    primos = 0
    for i in range(len(data)):
        if sympy.isprime(data[i]):
            primos += 1
    return primos

def resolve_trhread(data):
    ThreadsQtdd = 5
    tamanholista = len(data)
    index = range(0, tamanholista+(tamanholista//ThreadsQtdd), tamanholista//ThreadsQtdd)
    primos = 0
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(ThreadsQtdd):
            futures.append(executor.submit(tCalculaPrimo, data=data[index[i]:index[i+1]]))
        for future in concurrent.futures.as_completed(futures):
            #futures.append(future.result())
            primos += future.result()
    return primos
