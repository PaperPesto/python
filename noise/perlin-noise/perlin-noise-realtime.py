# https://pypi.org/project/perlin-noise/
# https://en.wikipedia.org/wiki/Perlin_noise

import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import numpy as np
import random

noise = PerlinNoise(octaves=10, seed=1)
xpix, ypix = 100, 100
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

pic = np.array(pic)
pic = np.floor((pic + 0.5) * 255)   # rinormalizzato tra 0 e 255

while 1:
    plt.imshow(pic, cmap='Blues')
    posx = random.randint(0, xpix - 1)
    posy = random.randint(0, ypix - 1)
    pic[posx,posy] = pic[posx,posy] - 100   # prendo un elemento a caso dalla matrice e ci tolgo 100, nell'immagine in tempo reale vedo dei pallini bianchi
    plt.pause(0.05)


plt.colorbar()  # non funziona...
plt.show()