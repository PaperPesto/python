import random
import matplotlib.pyplot as plt

def gen():
    map = [0] * 20
    pos = random.randint(0,19)
    map[pos] = 1
    return map

axislimits = [0,20,0,3]

map2 = [0] * 20
pos2 = random.randint(0,19)
map2[pos2] = 1

fig, axs = plt.subplots(4, figsize=(4,8))

fig.suptitle('Uniformly random generated')
axs[0].axis(axislimits)
axs[1].axis(axislimits)
axs[2].axis(axislimits)
axs[3].axis(axislimits)
axs[0].plot(gen(), 'bs')
axs[1].plot(gen(), 'rs')
axs[2].plot(gen(), 'gs')
axs[3].plot(gen(), 'ys')

plt.show()