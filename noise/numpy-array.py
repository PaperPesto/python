import numpy as np

# https://numpy.org/doc/stable/user/absolute_beginners.html

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(a[0])

# inzializzazione
np.ones(2)
np.zeros(2)
np.empty(2)
np.arange(4)
np.arange(2, 9, 2)

# array multidimensionali e tuple
array_example = np.array([[[0, 1, 2, 3],[4, 5, 6, 7]],[[0, 1, 2, 3],[4, 5, 6, 7]],[[0 ,1 ,2, 3],[4, 5, 6, 7]]])

array_example.ndim # numero di assi (dimensione): 3, ovvero una 3-pla (,,)
array_example.size # numero di elementi totali: 3*2*4 = 24
array_example.shape # tupla che comprende il numero di elementi per asse (3,2,4)

# da capire questo discorso, in particolare il (6,) senza niente dopo la virgola
a = np.array([1, 2, 3, 4, 5, 6])
b = np.expand_dims(a, axis=1)
print(b)
print(b.shape)