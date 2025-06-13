# imports
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import os


naam = 'maximumonder'
window_size = 5
midden_waarde = 6.87

os.chdir("C:\\Users\\luukj\\Documents\\GitHub\\project1.4\\meter")
naam_csv = naam + '.csv'


def lees_bestand(naam_csv):
    df = pd.read_csv(naam_csv)
    df.columns = df.columns.str.strip()  # verwijder spaties
    tijd = np.array(df['tijd'])
    uitwijking = np.array(df['uitwijking'])
    versnelling = np.array(df['versnelling'])
    return tijd,uitwijking,versnelling

def average(x):
    return np.average(x)

def rollingaverage(data):
    weights = np.ones(window_size) / window_size
    rolling_avg = np.convolve(data, weights, mode='same')
    return rolling_avg

def midden(data,waarde):
    midden = np.zeros(len(data))
    for i in range(len(data)):
        midden[i] = waarde
    return midden
def versnelling(y):
    m = 0.060
    k = 100
    a = np.zeros(len(y))
    for i in range(len(y)):
        a[i] = ((((y[i] - midden_waarde)/100) * k)/m)
    return a
t,y,a = lees_bestand(naam_csv) 
null = average(y)
a = versnelling(y)

y_roll = rollingaverage(y)
a_roll = rollingaverage(a)
midden_lijn = midden(t,midden_waarde)

plt.figure(0)
plt.scatter(t, y, label='Uitwijking')
plt.plot(t,y_roll,color='red',label='rolling average')
plt.plot(t,midden_lijn,color='purple',label='rust positie')
plt.xlabel("t")
plt.ylabel("y (cm)")
plt.title(naam + " uitwijking")
plt.tick_params(axis='y', labelcolor='blue')
plt.axhline(0, color='black', linestyle='solid', linewidth=0.8)
plt.legend(loc='lower right')
plt.grid()

plt.figure(1)
plt.scatter(t, a, label='versnelling',color='red')
plt.plot(t,a_roll,color='blue',label='rolling average')
plt.title(naam + " versnelling")
plt.xlabel("t")
plt.ylabel("a (m/s^2)")
plt.tick_params(axis='y', labelcolor='red')
plt.legend(loc='lower right')
plt.grid()
#ax1.set_ylim(-2, 2)
#ax2.set_ylim(-2, 2)

plt.show()