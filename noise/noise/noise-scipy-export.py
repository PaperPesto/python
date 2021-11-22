import noise
import numpy as np
import matplotlib.pyplot as plt
import math

shape = (32,32)
scale = 100.0
octaves = 6
persistence = 0.5
lacunarity = 2.0

world = np.zeros(shape)
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

content = ""

for i in range(shape[0]):
    for j in range(shape[1]):
        content = content + str(math.floor(world[i][j] * 256)) + ","
    
    content += "\n"

f = open("tilemap.txt", "w")
f.write(content)
f.close()