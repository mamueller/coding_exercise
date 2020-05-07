import numpy as np

def my_mean(X):
    return np.sum(X)/len(X)

def my_sample_cov(X,Y):
    return 1./(len(X)-1)*np.inner(X-my_mean(X),Y-my_mean(Y))

def my_sample_var(X):
    return my_sample_cov(X,X)

def my_sample_sig(X):
    return np.sqrt(my_sample_var(X))

def correlationCoefficient(X,Y):
    return my_sample_cov(X,Y) / (my_sample_sig(X)*my_sample_sig(Y))


