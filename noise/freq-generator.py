# sin wave
import random
import matplotlib.pyplot as plt
import math

mapsize = 200    # change this for increase detail
axislimits = [0, mapsize, -3, 3]
width = 1
fig, axs = plt.subplots(4)

amplitudes = [0.2, 0.5, 1.0, 0.7, 0.5, 0.4] # change frequency weight
frequencies = [1, 2, 4, 8, 16, 32]  # octaves

def noise(freq):
    phase = random.uniform(0, 2*math.pi)
    return [math.sin(2*math.pi * freq*x/mapsize + phase) for x in range(mapsize)]

def weighted_sum(amplitudes, noises):
    output = [0.0] * mapsize  # make an array of length mapsize
    for k in range(len(noises)):
        for x in range(mapsize):
            output[x] += amplitudes[k] * noises[k][x]
    return output


noises = [noise(f) for f in frequencies]
sum_of_noises   = weighted_sum([0.5, 0.0, 0.0, 0.0, 0.0, 0.5], noises)
sum_of_noises_0 = weighted_sum([1.0, 0.7, 0.5, 0.3, 0.2, 0.1], noises)
sum_of_noises_1 = weighted_sum([0.1, 0.1, 0.2, 0.3, 0.5, 1.0], noises)

# noises
#stampo solo la frequenza più bassa
axs[0].bar(range(len(noises[0])), noises[0], align='edge', width=width)
axs[0].set_title('low frequency only')
axs[0].axis(axislimits)
axs[0].xaxis.set_visible(False)

# sum_of_noises
axs[1].bar(range(len(sum_of_noises)), sum_of_noises, align='edge', width=width)
axs[1].set_title('sum_of_noises')
axs[1].axis(axislimits)
axs[1].xaxis.set_visible(False)

# sum_of_noises_0
axs[2].bar(range(len(sum_of_noises_0)), sum_of_noises_0, align='edge', width=width)
axs[2].set_title('sum_of_noises_0')
axs[2].axis(axislimits)
axs[2].xaxis.set_visible(False)

# sum_of_noises_1
axs[3].bar(range(len(sum_of_noises_1)), sum_of_noises_1, align='edge', width=width)
axs[3].set_title('sum_of_noises_1')
axs[3].axis(axislimits)
axs[3].xaxis.set_visible(False)

fig.suptitle('frequency generator')

# function to show the plot
plt.show()
