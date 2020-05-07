import unittest 
import timeit
from numba import njit,float64
import numpy as np

@njit
def my_mean(X):
    return np.divide(np.sum(X),X.shape[0])

@njit
def my_sample_cov(X,Y):
    n=X.shape[0]
    return np.divide(1.0,(n-1.0))*np.sum((X-my_mean(X))*(Y-my_mean(Y)))

@njit
def my_sample_var(X):
    return my_sample_cov(X,X)

@njit
def my_sample_sig(X):
    return np.sqrt(my_sample_var(X))

@njit
def correlationCoefficient(X,Y):
    return np.divide( my_sample_cov(X,Y) , (my_sample_sig(X)*my_sample_sig(Y)))


