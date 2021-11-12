import random
import matplotlib.pyplot as plt

def gen():
    map = [0] * 20  # make an empty map
    pos = random.randint(0, 19)  # pick a spot
    map[pos] = 1  # put the treasure there
    return map

y = []

for i in range(5):  # make 5 different maps
    # print_chart(i, gen())
    # x axis values
    # corresponding y axis values
    y.append(random.randint(0, 19))

x = [0,1,2,3,4]

plt.plot(x, y)
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()