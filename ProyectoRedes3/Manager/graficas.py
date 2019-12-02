# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 00:56:43 2019

@author: navi_
"""

import matplotlib.pyplot as plt

def get_values(filename):
    values = []
    with open(filename, 'r') as f:
        values = f.read().split(',')
    return values

def cpu_graph(hostname):        
    
    cpu = get_values('static/values/'+ hostname + '_cpu.txt')
    cpu_values = []
    for v in cpu:
        cpu_values.append(float(v))
        
    t = range(0, 25, 1)
    
    fig, ax = plt.subplots()
    ax.plot(t, cpu_values)
    ax.set(xlabel='Tiempo (hrs)', ylabel='Uso de CPU (%)',
           title='Uso del CPU en '+ hostname + ' durante el última día')
    ax.grid()
    fig.savefig('static/graphs/CPU_'+hostname+'.png')
    plt.ylim(0,20)
    plt.legend()
    plt.show()
