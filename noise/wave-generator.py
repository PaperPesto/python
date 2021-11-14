# wave generator
import random
import matplotlib.pyplot as plt
import math

mapsize = 200    # change this for increase detail
axislimits = [0, mapsize, -3, 3]
width = 1
fig, axs = plt.subplots(5)
frequencies = range(1, 31)  # [1, 2, ..., 30]


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

# Red noise is f^-1
# Pink noise is f^-½
# White noise is f^0
# Blue noise is f^+½
# Violet noise is f^+1

red_noise = random_ift(lambda f: 1/f)
pink_noise = random_ift(lambda f: 1/math.sqrt(f))
white_noise = random_ift(lambda f: 1)
blue_noise = random_ift(lambda f: math.sqrt(f))
violet_noise = random_ift(lambda f: f)


# red_noise
axs[0].bar(range(len(red_noise)), red_noise, align='edge', width=width)
axs[0].set_title('red_noise')
axs[0].axis(axislimits)
axs[0].xaxis.set_visible(False)

# pink_noise
axs[1].bar(range(len(pink_noise)), pink_noise, align='edge', width=width)
axs[1].set_title('pink_noise')
axs[1].axis(axislimits)
axs[1].xaxis.set_visible(False)

# white_noise
axs[2].bar(range(len(white_noise)), white_noise, align='edge', width=width)
axs[2].set_title('white_noise')
axs[2].axis(axislimits)
axs[2].xaxis.set_visible(False)

# blue_noise
axs[3].bar(range(len(blue_noise)), blue_noise, align='edge', width=width)
axs[3].set_title('blue_noise')
axs[3].axis(axislimits)
axs[3].xaxis.set_visible(False)

# violet_noise
axs[4].bar(range(len(violet_noise)), violet_noise, align='edge', width=width)
axs[4].set_title('violet_noise')
axs[4].axis(axislimits)
axs[4].xaxis.set_visible(False)

fig.suptitle('frequency generator')

# function to show the plot
plt.show()
