# https://pypi.org/project/perlin-noise/
# https://en.wikipedia.org/wiki/Perlin_noise

import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import numpy as np

noise = PerlinNoise(octaves=10, seed=1)
xpix, ypix = 100, 100
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

pic = np.array(pic)
pic = np.floor((pic + 0.5) * 255)   # rinormalizzato tra 0 e 255

plt.imshow(pic, cmap='Blues')
plt.colorbar()
plt.show()