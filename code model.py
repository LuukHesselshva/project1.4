# imports
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

#csv naam
naam_csv = 'versnellingsprofiel_scherp.csv'
output_csv_naam = 'data'
# start waarde
massa = 0.50 # in kg
veer_constante = 50 # N/m
demmpingsfactor = np.sqrt(4*massa*veer_constante) # Kg/s
x0 = 0 # m
v0 = 0 # m/s
F0 = 0 # N0

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
    tijd = np.array(df['# tijd (s)'])
    versnelling = np.array(df['versnelling (m/s^2)'])
    kracht = versnelling * massa
    return tijd,kracht

def model(t,m,b,k,x0,v0,F):
    l = len(t)
    x = np.zeros(l)
    v = np.zeros(l)
    a = np.zeros(l)
    F_ext = np.zeros(l)
    x[0],v[0] = x0, v0
    for i in range(len(F)):
        F_ext[i] = F[i]

    for i in range(l - 1):
        a[i] = (F_ext[i] - b * v[i] - k * x[i]) / m
        v[i + 1] = v[i] + a[i] * dt
        x[i + 1] = x[i] + v[i] * dt
    a_sensor = (x * k)/m

    a[-1] = (F_ext[-1] - b * v[-1] - k * x[-1]) / m
    return x, v, a, a_sensor

t, F = lees_bestand(naam_csv)
#t = tijd
x, v, a, a_sensor= model(t,massa,demmpingsfactor,veer_constante,x0,v0,F)
versnelling_stim = F / massa

df_out = pd.DataFrame({
    'Tijd' : [t],
    'positie' : [x],
    'versnelling_sensor' : [a_sensor],
    'versnelling_stim' : [versnelling_stim]
})

df_out.to_csv(output_csv_naam)

plt.figure(0)
#plt.plot(t,v,label='snelheid(m/s)')
#plt.plot(t,a,label='versnelling(m/s^2)')
plt.plot(t,a_sensor,label='versnelling sensor(m/s^2)',color='orange')
plt.plot(t,versnelling_stim,label='stimulus(m/s^2)',color='red')
plt.xlabel('Tijd (s)')
plt.ylabel('versnelling (m/s^2)')
plt.title('model van de sensor')
plt.legend()
plt.grid(True)

plt.figure(1)
plt.plot(t,x,label='positie(m)',color ='blue')
plt.title('model van de sensor')
plt.xlabel('Tijd (s)')
plt.ylabel('afstand (m)')
plt.legend()
plt.grid()

plt.show()
