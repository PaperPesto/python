import numpy as np

# https://numpy.org/doc/stable/user/absolute_beginners.html

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
#print(a[0])

# inzializzazione
np.ones(2)
np.zeros(2)
np.empty(2)
np.arange(4)
np.arange(2, 9, 2)

# indexing
a0 = np.array([1,2,3,4,5])
# print(a0[1])
# print(a0[0:3])


# array multidimensionali e tuple
array_example = np.array([[[0, 1, 2, 3],[4, 5, 6, 7]],[[0, 1, 2, 3],[4, 5, 6, 7]],[[0 ,1 ,2, 3],[4, 5, 6, 7]]])

array_example.ndim # numero di assi (dimensione): 3, ovvero una 3-pla (,,)
array_example.size # numero di elementi totali: 3*2*4 = 24
array_example.shape # tupla che comprende il numero di elementi per asse (3,2,4)

# da capire questo discorso, in particolare il (6,) senza niente dopo la virgola
a1 = np.array([1, 2, 3, 4, 5, 6])
b1 = np.expand_dims(a1, axis=1)
#print(b1)
#print(b1.shape)


# shape
# https://stackoverflow.com/questions/22053050/difference-between-numpy-array-shape-r-1-and-r
# --------------------------------------------------------------------------------------------
# internamento numpy salva gli array come numeri raw
# gli shape descrivono la vista che uno utilizza per recuperare tali numeri
# a.shape = (x,y) a[i][j] interroga questa vista sullo stesso data seta
# a.shape = (x,) a[i] funziona mentre a[i][j] non funziona
# a.reshape((x,y,x)) crea una nuova vista con 3 indici e posso accedere ai dati con a[i][j][k]
a2 = np.array([1,2,3,4,5,6,7,8])
print(a2.shape)
b2 = a2.reshape((1,8))
print(b2.shape)