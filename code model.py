# imports
import numpy as np
import matplotlib.pyplot as plt
import math

# start waarde
massa = 1 # in kg
demmpingsfactor = 1 # Kg/s
veer_constante = 1 # N/m
x0 = 0 # m
v0 = 0 # m/s
F0 = 0 # Ns

# tijd(s)
t0 = 0
teind = 10
dt = 0.01
nt = int((teind - t0)/ dt)
tijd = np.linspace(t0,teind,nt)

#kritische demp
b_krit = math.sqrt(4*massa*veer_constante)

def model(t,m,b,k,x0,v0):
    pass

print("test")