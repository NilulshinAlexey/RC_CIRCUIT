import matplotlib.pyplot as plt

l = list()

for i in range(0, 100, 1):
    l.append((i/10) ** 0.5)

str_list = [str(i) for i in l]

with open('values.txt', 'w') as f:
    f.write('\n'.join(str_list))

plt.tick_params(axis='both', which='major', labelsize=16, size=10)
plt.grid(visible = True, linewidth = 0.6)
plt.plot(l)
plt.show()

print('Finish')