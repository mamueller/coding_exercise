import timeit
import numpy as np
import unittest 
from matplotlib import pyplot as plt
from mod_names import  all_mod_names
import importlib

def measure_time(name):
    mod=importlib.import_module(name) 
    n=100000
    # Driver function 
    X = np.array([x for x in range(n)])
    Y = np.array([1.3*x for x in range(n)])
    fun=lambda:getattr(mod,'correlationCoefficient')(X,Y) 
    # call once to activate the numba compiler outside the measurement
    fun()
    print("#######################################################################")
    print("module name:",mod.__name__)
    t=timeit.timeit(fun, number=100)
    print("time: ",t)
    return t

plt.rcParams.update({'figure.autolayout': True})
fig,axs = plt.subplots(
    nrows=1
    ,ncols=1
    ,figsize = ( 11.69, 8.27)
)
times=[measure_time(name) for name in all_mod_names]
y_pos=[y for y,_ in enumerate(all_mod_names)]
axs.barh(y_pos,times,log=True,tick_label=all_mod_names)
axs.invert_yaxis()
axs.set(xlabel='run time',ylabel='module name')
fig.savefig('profiling.pdf')
