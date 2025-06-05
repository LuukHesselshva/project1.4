# imports
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

naam_csv = 'test.csv'

def lees_bestand(naam_csv):
    df = pd.read_csv(naam_csv)
    df.columns = df.columns.str.strip()  # verwijder spaties
    tijd = np.array(df['tijd'])
    uitwijking = np.array(df['uitwijking'])
    versnelling = np.array(df['versnelling'])
    return tijd,uitwijking,versnelling

t,y,a = lees_bestand(naam_csv) 

plt.figure(0)
plt.scatter(t, y, label='Uitwijking')
plt.xlabel("t")
plt.ylabel("y (cm)", color='blue')
plt.tick_params(axis='y', labelcolor='blue')
plt.axhline(0, color='black', linestyle='solid', linewidth=0.8)
plt.grid()

plt.figure(1)
plt.scatter(t, a, label='versnelling',color='red')
plt.xlabel("t")
plt.ylabel("a (m/s^2)", color='red')
plt.tick_params(axis='y', labelcolor='red')
plt.grid()
#ax1.set_ylim(-2, 2)
#ax2.set_ylim(-2, 2)

plt.show()