import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator 


with open('settings.txt', 'r') as set:
    sets = [float(i) for i in set.read().split('\n')]

with open('data.txt', 'r') as data:
    values = np.array([int(i) for i in data.read().split('\n')]) * 3.3/256

time = np.arange(0, len(values)) * sets[1]

fig, ax = plt.subplots (figsize = (16, 10), dpi = 400)

mark_v = []
mark_t = []

for i in range (50, len(values), 50):
    mark_v = values[i]
    mark_t = time[i]

mark_v = np.array(mark_v)
mark_t = np.array(mark_t)

ax.set_ylabel("Напряжение, В", fontsize = 15)
ax.set_xlabel("Всремя, с", fontsize = 15)
ax.set_title("График зависимости U(t)", fontsize = 20)
ax.grid(visible = True, which = 'major', linewidth = 1, linestyle = '-.')
ax.text(7, 2, 'Вермя зарядки 4.21 c', fontsize = 15)
ax.text(7, 1.5, 'Вермя разрядки 5.65 c', fontsize = 15)

ax.plot(time, values, marker = 'o', markevery = 50, c = 'red', linewidth = 2, label = 'U(t)')

ax.legend(fontsize = 20)
fig.savefig('plot.png')