# https://medium.com/@yvanscher/playing-with-perlin-noise-generating-realistic-archipelagos-b59f004d8401
# https://stackoverflow.com/questions/27600640/how-to-save-a-3-channel-numpy-array-as-image

import noise
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import cm

# Colori RGB
blue = [65,105,225]
green = [34,139,34]
beach = [238, 214, 175]

# Parametri Perlin Noise
shape = (256,256)
scale = 300.0
octaves = 6
persistence = 0.5
lacunarity = 2.0

# Prende un array (X,Y) e restituisce un array (X,Y,3) con le informazioni dei colori rgb
def add_color(world):
    color_world = np.zeros(world.shape+(3,), dtype=np.uint8)    # usare uint8 per la 3-pla dei colori
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.05:
                color_world[i][j] = blue
            elif world[i][j] < 0:
                color_world[i][j] = beach
            elif world[i][j] < 1.0:
                color_world[i][j] = green

    return color_world

# Inizializzazione mondo
world = np.zeros(shape)

# Generazione mondo con perlin noise
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = noise.pnoise2(i/scale, 
                                    j/scale, 
                                    octaves=octaves, 
                                    persistence=persistence, 
                                    lacunarity=lacunarity, 
                                    repeatx=1024, 
                                    repeaty=1024, 
                                    base=0)

color_world = add_color(world)

# Salvataggio in pgn. Attenzione all'ordine delle shape (vedi doc in alto)
img = Image.fromarray(color_world, 'RGB')
img.save('world.png')

# Mostra il grafico in 3D
# X=np.arange(shape[0])
# Y=np.arange(shape[1])
# X, Y = np.meshgrid(X, Y)
# pic = np.array(world)

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# surf = ax.plot_surface(X, Y, pic, cmap=cm.coolwarm, linewidth=0, antialiased=False)
# fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.title('z as 3d height map')
# plt.show()