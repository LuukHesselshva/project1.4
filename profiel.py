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

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(t, y, 'b-', label='Uitwijking')
ax1.set_xlabel("t")
ax1.set_ylabel("y (cm)", color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax1.axhline(0, color='black', linestyle='solid', linewidth=0.8)

ax2 = ax1.twinx()
ax2.plot(t, a, 'r-', label='versnelling')
ax2.set_ylabel("a (m/s^2)", color='red')
ax2.tick_params(axis='y', labelcolor='red')

#ax1.set_ylim(-2, 2)
#ax2.set_ylim(-2, 2)

fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
plt.show()