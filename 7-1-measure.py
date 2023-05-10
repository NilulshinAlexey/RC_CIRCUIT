import matplotlib.pyplot as plt
import numpy as np

my_list = []

for i in range(0, 100, 1):
    my_list.append((i/10) ** 0.5)

my_list = np.array(my_list)
time = np.arange(0, 100, 1) / 10

str_list = [str(i) for i in my_list]

with open('values.txt', 'w') as f:
    f.write('\n'.join(str_list))

plt.title("Мой грффик", fontsize = 12)
plt.grid(visible = True, linewidth = 0.6)
plt.plot(time, my_list, 'r-')
plt.show()

print('Finish')