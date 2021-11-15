# wave generator
import random
import matplotlib.pyplot as plt
import math
import numpy as np

mapsize = 256    # change this for increase detail
axislimits = [0, mapsize, -3, 3]
width = 1
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(16, 5))
frequencies = range(1, 8)


def noise(freq):
    phase = random.uniform(0, 2*math.pi)
    return [math.sin(2*math.pi * freq*x/mapsize + phase) for x in range(mapsize)]


def weighted_sum(amplitudes, noises):
    output = [0.0] * mapsize  # make an array of length mapsize
    for k in range(len(noises)):
        for x in range(mapsize):
            output[x] += amplitudes[k] * noises[k][x]
    return output


def random_ift(amplitude):
    amplitudes = [amplitude(f) for f in frequencies]
    noises = [noise(f) for f in frequencies]
    sum_of_noises = weighted_sum(amplitudes, noises)
    return sum_of_noises


# noisex = random_ift([0.8,0.5,0.4,0.2,0.3,0.4,0.2,0.3])
# noisey = random_ift([0.9,0.8,0.1,0.2,0.3,0.4,0.2,0.3])
noisex = random_ift(lambda f: 1/(f*f))
noisey = random_ift(lambda f: 1/(f*f))

npx = np.array(noisex, dtype=np.float32)
npy = np.array(noisey, dtype=np.float32)

heightmap = np.zeros((mapsize, mapsize))

for i in range(mapsize):
    for j in range(mapsize):
        heightmap[i][j] = npx[i]*npy[j]



# red_noise
axs[0].bar(range(len(noisex)), noisex, align='edge', width=width)
axs[0].set_title('noisex')
axs[0].axis(axislimits)
axs[0].xaxis.set_visible(False)

# noisey
axs[1].bar(range(len(noisey)), noisey, align='edge', width=width)
axs[1].set_title('noisey')
axs[1].axis(axislimits)
axs[1].xaxis.set_visible(False)

# mesh
axs[2].pcolormesh(heightmap.real)

fig.suptitle('heightmap')

# function to show the plot
plt.show()
