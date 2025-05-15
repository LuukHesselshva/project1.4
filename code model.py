# imports
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

#csv naam
naam_csv = 'versnellingsprofiel_scherp.csv'

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

def lees_bestand(naam_csv):
    df = pd.read_csv(naam_csv)
    df.columns = df.columns.str.strip()  # verwijder spaties
    #df = df.rename(columns={'# tijd (s)': 'tijd', 'versnelling (m/s^2)': 'versnelling'})
    tijd = np.array(df['# tijd (s)'])
    versnelling = np.array(df['versnelling (m/s^2)'])
    #print('tijd',tijd)
    #print('versnelling',versnelling)
    return tijd,versnelling

def model(t,m,b,k,x0,v0,f):
    l = len(t)
    x = np.zeros(l)
    v = np.zeros(l)
    a = np.zeros(l)

    x[0],v[0] = x0, v0
    
    F_ext = massa * f

    for i in range(l - 1):
        a[i] = (F_ext[i] - b * v[i] - k * x[i]) / m
        v[i + 1] = v[i] + a[i] * dt
        x[i + 1] = x[i] + v[i] * dt

    a[-1] = (F_ext[-1] - b * v[-1] - k * x[-1]) / m
    return x, v, a

t, f = lees_bestand(naam_csv)

x, v, a = model(t,massa,demmpingsfactor,veer_constante,x0,v0,f)
plt.plot(t,x)
plt.plot(t,v)
plt.plot(t,a)
plt.show()
