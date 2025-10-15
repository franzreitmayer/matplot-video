import numpy as np

import scipy.special

import matplotlib.pyplot as plt

import matplotlib.animation as animation

import math


 

# Funktion definieren

def f(x):

    return scipy.special.factorial(np.round(x))

 
def g(x):
    return x**2

def h(x):
    return 5 * x

# Datenbereich

x = np.linspace(0, 800, 200)

 

# Setup der Grafik

plt.rcParams['text.color'] = 'xkcd:gray'
plt.rcParams['axes.labelcolor'] = 'xkcd:gray'
plt.rcParams['axes.edgecolor'] = 'xkcd:gray'
plt.rcParams['xtick.color'] = 'xkcd:gray'
plt.rcParams['ytick.color'] = 'xkcd:gray'

fig, ax = plt.subplots()


fig.set_facecolor('xkcd:black')

ax.set_facecolor('xkcd:black')

line, = ax.plot([], [], lw=2)

line2, = ax.plot([], [], lw=2)

line3, = ax.plot([], [], lw=2)

ax.set_xlim(0, 800)

ax.set_ylim(0, 10000)

 

# Initialisierung

def init():

    line.set_data([], [])

    return line,

 

# Update-Funktion für jedes Frame

def update(frame):

    x_data = x[:frame]

    y_data = f(x_data)

    y2_data = g(x_data)

    y3_data = h(x_data)

    line.set_data(x_data, y_data)

    line2.set_data(x_data, y2_data)

    line3.set_data(x_data, y3_data)

    return line,

 
# "C:\usr\ffmpeg\bin\ffmpeg.exe"
# Animation erstellen
plt.rcParams['animation.ffmpeg_path'] = 'C:\\usr\\ffmpeg\\bin\\ffmpeg.exe'

ani = animation.FuncAnimation(fig, update, frames=len(x), init_func=init, blit=True)

 

# Video speichern

# ani.save("sine_wave.mp4", fps=30, extra_args=['-vcodec', 'libx264'])


writervideo = animation.FFMpegWriter(fps=30)

ani.save("vid.mp4", writer=writervideo)

