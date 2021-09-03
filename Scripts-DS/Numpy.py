#Importamos las librerias de array y numpy
import array as a
import numpy as np

L = list(range(10))
A = a.array('i',L)
print(A)

#Creacion de arreglos desde listas de python
print(np.array([1,2,3,4,5],dtype='float32'))

#Creacion de arreglos multidimensionales
print(np.array([range(i,i+3) for i in [2,4,6]]))

print(np.ones((3,5),dtype='float'),'\n')
print(np.zeros((4,3),dtype='float32'),'\n')
print(np.full((2,3),3.14),'\n')

#Creacion de arrays con secuencia lineal
#Inicia en 0 hasta 20 con paso de 2
print(np.arange(0,20,2),'\n')

#Inicia en 0, termina en 1 dividido en 5 subdivisiones
print(np.linspace(0,1,5),'\n')

#Creacion de array 3 x 3 con valores aleatorios de 0 a 1
print(np.random.random((3,3)))