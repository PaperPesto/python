import random
import matplotlib.pyplot as plt

def gen():
    map = [0] * 20
    pos = random.randint(0,19)
    map[pos] = 1
    return map

def gen_array(rnd, div):
    map = [0] * 20
    pos = rnd // div
    map[pos] = 1
    return map

axislimits = [0,20,0,4]
width=1

fig, axs = plt.subplots(4)

# Set the ticks and ticklabels for all axes
# plt.setp(axs, xticks=[0.1, 0.5, 0.9], xticklabels=['a', 'b', 'c'], yticks=[1, 2, 3])

#decommentare per partire da una distribuzione flat per vedere 4 distribuzioni diverse
# rnd = random.randint(0,19)
# bars0 = gen_array(rnd, 1)
# bars1 = gen_array(rnd, 2)
# bars2 = gen_array(rnd, 3)
# bars3 = gen_array(rnd, 4)
bars0 = gen()
bars1 = gen()
bars2 = gen()
bars3 = gen()
axs[0].bar(range(len(bars0)), bars0, align='edge', width=width, color='red')
axs[1].bar(range(len(bars1)), bars1, align='edge', width=width, color='orange')
axs[2].bar(range(len(bars2)), bars2, align='edge', width=width, color='green')
axs[3].bar(range(len(bars3)), bars3, align='edge', width=width, color='blue')
axs[0].axis(axislimits)
axs[1].axis(axislimits)
axs[2].axis(axislimits)
axs[3].axis(axislimits)
axs[0].xaxis.set_visible(False)
axs[1].xaxis.set_visible(False)
axs[2].xaxis.set_visible(False)
axs[3].xaxis.set_visible(False)

fig.suptitle('Uniformly randafom generated')

# function to show the plot
plt.show()