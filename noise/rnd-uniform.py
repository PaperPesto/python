import random
import matplotlib.pyplot as plt

map = [0] * 20
pos = random.randint(0,19)
map[pos] = 1

plt.plot(map, 'ro')

# giving a title to my graph
plt.title('Random uniform')

# function to show the plot
plt.show()