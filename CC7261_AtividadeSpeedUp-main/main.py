from time import perf_counter_ns
import simples as sp
import mtrhead as mt

with open("data.csv") as file:
    data = [line.strip() for line in file]

data = list(map(int, data))

print('\n\nanalise de %d valores\n\n'%(len(data)))
start1 = perf_counter_ns()
primo_sp = sp.resolve_simples(data)
finish1 = perf_counter_ns()

start2 = perf_counter_ns()
primo_mt = mt.resolve_trhread(data)
finish2 = perf_counter_ns()

print('simples          > threads')
print('%f ms   > %f ms  : tempo execucao'%((finish1-start1)/1000000,(finish2-start2)/1000000))
print('%d            > %d           :numeros primos encontrados'%(primo_sp,primo_mt))

