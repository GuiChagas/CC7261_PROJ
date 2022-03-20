from time import perf_counter_ns
import simples as sp
import mtrhead as mt
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import statistics


def main():
    global speedupForThread

    speedupForThread = {}

    thread_num = 5
    data = openFile()

    for i in range(10):
        execThread(data, thread_num)
        thread_num += 5

    #GRAPH speedUp
     fig, ax = plt.subplots()
     ax.plot(speedupForThread.keys(), speedupForThread.values())
     plt.show()

def openFile():
    with open("data1.csv") as file:
        data = [line.strip() for line in file]

    data = list(map(int, data))

    return data


def execThread(data, thread_num):
    simple_time_array = []
    simple_speed_array = []
    thread_time_array = []
    thread_speed_array = []
    for tests in range(20):
        start1 = perf_counter_ns()
        primo_sp = sp.resolve_simples(data)
        finish1 = perf_counter_ns()

        simple_time = (finish1 - start1) / 1000000
        
        print("simple time - test: %d -> %f" % (tests, simple_time))
        simple_time_array.append(simple_time)
        simple_speed_array.append((finish1 - start1))

    while 1:
        print('\n\nanalise de %d valores\n\n'%(len(data)))

        thread_time_array = []
        
        for tests in range(20):
            start2 = perf_counter_ns()
            primo_mt = mt.resolve_trhread(data, thread_num)
            finish2 = perf_counter_ns()

            thread_time = (finish2 - start2) / 1000000
            
            print("thread time - test: %d -> %f" % (tests, thread_time))

            thread_time_array.append(thread_time)
            thread_speed_array.append((finish2 - start2))
            

        speedUp = (statistics.mean(simple_speed_array) / statistics.mean(thread_speed_array))
        fracaoSerial = ((100 * thread_num) / speedUp) / (thread_num - 1)
        speedupForThread[thread_num] = speedUp 
        
        print('simples          > threads = %d' % thread_num)
        print('%f ms   > %f ms  : tempo execucao' % (statistics.mean(simple_time_array), statistics.mean(thread_time_array)))
        print('%d            > %d           :numeros primos encontrados' % (primo_sp,primo_mt))
        print('speedUp= %f' % speedUp)
        print('fração serial= %f' % fracaoSerial)
        
        #GRAPH tempo de exec
         fig, ax = plt.subplots()
         ax.plot(simple_time_array, label='time simple')
         ax.plot(thread_time_array, label= 'time thread')
         plt.show()

        break

        if statistics.mean(simple_time_array) < statistics.mean(thread_time_array):
            break

main()
