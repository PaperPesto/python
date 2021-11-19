import sys
from noise import pnoise2, snoise2
import matplotlib.pyplot as plt

if len(sys.argv) not in (2, 3) or '--help' in sys.argv or '-h' in sys.argv:
	print('2dtexture.py FILE [OCTAVES]')
	print()
	print(__doc__)
	raise SystemExit


if len(sys.argv) > 2:
	octaves = int(sys.argv[2])
else:
	octaves = 1
freq = 16.0 * octaves


for y in range(256):
	for x in range(256):
		int(pnoise2(x / freq, y / freq, octaves, persistence=0.5, lacunarity=2.0) * 127.0 + 128.0)

plt.imshow(pic, cmap='gray')
plt.show()
