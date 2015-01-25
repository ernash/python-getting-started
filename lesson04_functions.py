import numpy as np
import matplotlib.pyplot as plt


'''
    Draws a the x-axis and the y-axis on the canvas and also fixes the limits of
    the x-axis (without this the x-axis will be approximated to the nearest
    integer, but in this example it is 2 pi, which will result in the function
    being not drawn on the canvas at the beginning and end)
'''
def nice_subplot(min, max):
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.xlim(min, max)

max = 2 * np.pi
min = -max
num = (abs(min) + abs(max)) * 10

x = np.linspace(min, max, num)

figure = plt.figure()

plt.subplot(211)
nice_subplot(min, max)

sin = plt.plot(x, np.sin(x), 'b-')
cos = plt.plot(x, np.cos(x), 'r-')

plt.subplot(212)
# without the axes and the fixed x-axis limit

sin = plt.plot(x, np.sin(x), 'b-')
cos = plt.plot(x, np.cos(x), 'r-')

plt.show()
