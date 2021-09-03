#Importamos las librerias de array y numpy
import array as a
import numpy as np

L = list(range(10))
A = a.array('i',L)
print(A)

#Creacion de arreglos desde listas de python
print(np.array([1,2,3,4,5],dtype='float32'))
