import numpy as np
import matplotlib.pyplot as plt

def stdev(input):
    return np.std(input)
def average(input):
    return np.mean(input)
def linear_fit(a,x,b):
    return a*x+b

ref = np.array([3,5,7,9,11,13,15,17])
sensor = np.array([
    [3.07,3.01,3.09,2.86,2.85],
    [4.979,4.979,4.997,4.96,4.97],
    [6.880,6.883,6.883,6.865,7.014],
    [9.180,9.010,8.975,8.956,9.010],
    [10.879,11.120,11.070,10.896,11.080],
    [13.190,13.190,13.190,13.211,13.190],
    [14.446,15.732,14.480,15.710,14.446],
    [17.429,17.296,16.570,16.384,17.636]
])

sensor_average = np.array([
    average(sensor[0]),
    average(sensor[1]),
    average(sensor[2]),
    average(sensor[3]),
    average(sensor[4]),
    average(sensor[5]),
    average(sensor[6]),
    average(sensor[7]),
])
sensor_stdev = np.array([
    stdev(sensor[0]),
    stdev(sensor[1]),
    stdev(sensor[2]),
    stdev(sensor[3]),
    stdev(sensor[4]),
    stdev(sensor[5]),
    stdev(sensor[6]),
    stdev(sensor[7]),
])
a, b = np.polyfit(ref, sensor_average, deg=1)
xbegin, xeind, xstap = (ref[0]-5),(ref[len(ref)-1]+5), 10
x_array = np.linspace(xbegin,xeind,xstap)
y_array = x_array
trendline = linear_fit(a,ref,b)

plt.plot(x_array,y_array,linestyle='--',color='red')
plt.plot(ref,trendline,linestyle='--',color='blue')
plt.scatter(ref,sensor_average)
plt.errorbar(ref,sensor_average,yerr=sensor_stdev,linestyle='None')
plt.xlim((ref[0]-2),(ref[len(ref)-1]+2))
plt.ylim((sensor_average[0]-2),(sensor_average[len(sensor_average)-1]+2))

plt.xlabel("referentie data(cm)"), plt.ylabel("gemeten data(cm)"), plt.title('kalibratie van de sensor'), plt.grid()
plt.show()

