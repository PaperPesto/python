# https://pypi.org/project/perlin-noise/
# https://en.wikipedia.org/wiki/Perlin_noise

import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import numpy as np
from matplotlib import cm

noise = PerlinNoise(octaves=4, seed=1)
xpix, ypix = 100, 100
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

X=np.arange(xpix)
Y=np.arange(ypix)
X, Y = np.meshgrid(X, Y)
pic = np.array(pic)

# show hight map in 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, pic, cmap=cm.coolwarm, linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.title('z as 3d height map')
plt.show()