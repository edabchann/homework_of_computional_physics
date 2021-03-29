import matplotlib.pyplot as plt
import numpy as np
import math

def ff(function, *args, center=0):
    y_ff = []
    for h in args:
        y_ff.append((function(center + h)-function(center))/h)
    return y_ff

def fb(function, *args, center=0):
    y_fb = []
    for h in args:
        y_fb.append((function(center)-function(center - h))/h)
    return y_fb

def fc(function, *args, center=0):
    y_fc = []
    for h in args:
        y_fc.append((function(center + h)-function(center - h))/(2*h))
    return y_fc

def function(x):
    return x*math.exp(x)

if __name__ == '__main__':
    x = np.linspace(0.00001, 0.00002, 100)
    y_ff = ff(function, *x, center=2)
    y_fb = fb(function, *x, center=2)
    y_fc = fc(function, *x, center=2)
    precise_deriv = 3*math.exp(2)
    plt.figure()
    plt.plot(x, y_ff, label='ff')
    plt.plot(x, precise_deriv+2*x*math.exp(2), label='ff_expectation', linestyle='--')
    plt.plot(x, y_fb, label='fb')
    plt.plot(x, precise_deriv-2*x*math.exp(2), label='ff_expectation', linestyle='--')
    plt.plot(x, y_fc, label='fc')
    plt.axhline(y=precise_deriv, label='precise', linestyle='--')
    plt.xlabel('h')
    plt.ylabel('approx of deriv')
    plt.legend()
    plt.show()
    

