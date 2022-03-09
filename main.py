from time import perf_counter_ns
import simples as sp
import mtrhead as mt
import statistics

with open("data1.csv") as file:
    data = [line.strip() for line in file]

data = list(map(int, data))

thread_num = 5

simple_time_array = []
thread_time_array = []

for tests in range(10):
    start1 = perf_counter_ns()
    primo_sp = sp.resolve_simples(data)
    finish1 = perf_counter_ns()

    simple_time = (finish1 - start1) / 1000000

    print("simple time - test: %d -> %f" % (tests, simple_time))
    simple_time_array.append(simple_time)

while 1:
    print('\n\nanalise de %d valores\n\n'%(len(data)))

    thread_time_array = []

    for tests in range(10):
        start2 = perf_counter_ns()
        primo_mt = mt.resolve_trhread(data, thread_num)
        finish2 = perf_counter_ns()

        thread_time = (finish2 - start2) / 1000000
        
        print("thread time - test: %d -> %f" % (tests, thread_time))

        thread_time_array.append(thread_time)

    print('simples          > threads = %d' % thread_num)
    print('%f ms   > %f ms  : tempo execucao' % (statistics.mean(simple_time_array), statistics.mean(thread_time_array)))
    print('%d            > %d           :numeros primos encontrados' % (primo_sp,primo_mt))

    if statistics.mean(simple_time_array) < statistics.mean(thread_time_array):
        break

    thread_num += 1

