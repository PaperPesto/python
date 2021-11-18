import matplotlib.pyplot as plt
import numpy as np

# https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html

# caso 1
a = np.fft.ifft([0, 4, 0, 0, 0, 0, 0, 0])

plt.plot(a.real)
plt.show()


#caso 2
t = np.arange(400)
n = np.zeros((400,), dtype=complex)