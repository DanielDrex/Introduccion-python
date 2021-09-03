#En python la identacion es importante
if 3 > 5:
    print('Esto no se va a imprimir')

if 5 > 3:
    print('5 es mayor que 3')

x = 5
y = 'cadena'

#print(x,y)

email = 'test@tester.com'
password = 'tester'
nameUser = 'george'
#print(email,password, nameUser)

#Multiples variables con distinto valor"
a, b, c = 'var1', 'var2', 'var3'
#print(a,b,c)

#Multiples variables con el mismo valor#
valor1 = valor2 = valor3 = 'un solo valor para 3 variables'
#print(valor1)
#print(valor2)
#print(valor3)

#Concatenacion de variables#
inicio = 'Hola '
final = 'mundo'

#print(inicio+final)

#Tipos de datos#

palabra = 'hola mundo' #string
oracion = "hola mundo comilla doble" #string

entero = 20 #integer
conDecimal = 20.2 #float
complejo = 1j

#print(palabra,oracion,entero, conDecimal, complejo)

#-----------------LISTAS--------------------
lista = [1,2,3]
lista2 = lista.copy()
lista.append(4)
#lista.clear()

#lista.count(2) este metodo nos cuenta cuantas veces esta el elemento indicado en la lista
print(lista,lista2.count(3))
#len(lista) este metodo nos regresa el tamaño de la lista o arreglo indicado
print(len(lista),len(lista2))
#Indicamos el indice del elemento de la lista
print(lista[0])
#pop() nos elimina el ultimo elemento de la lista
lista.pop()
print(lista)
#Metodo que nos ayuda a eliminar el elemento indicado de la lista
#lista.remove(2)
#reverse() nos ayuda a invertir la lista
lista.reverse()
print(lista)
#aort() metodo que nos ayuda a ordenar listas
lista.sort()
print(lista)

#TUPLAS
#Las tuplas tienen los metodos de count() y de index []
tupla = ('hola','mundo','somos','tupla')
print(tupla,tupla[2])

#TRANSFORMAR TUPLA A LISTA
listadeTupla = list(tupla)
listadeTupla.append('nuevo')
print(listadeTupla)

#RANGOS

rango = range(6)
print(rango)

s = 'abc'
h = 'bca'
print(s.__sizeof__())
print(h.__sizeof__())

#DICCIONARIOS
diccionario = {"nombre":"Chanchito feliz",
                "raza": "Persa",
                "edad": 5
}
print(diccionario,diccionario.get("nombre"))
diccionario["nombre"]="Tod"
#Obtener datos de un diccionarrio con get()
print(diccionario.get("nombre"))
diccionario['ronronea'] = 'si'
print(diccionario)
#Eliminacion de propiedades del diccionario
#diccionario.pop('ronronea')
print(diccionario)
#diccionario.popitem()
print(diccionario)
del diccionario['ronronea']
print(diccionario)
#Copias de un diccionario
copiaDic = diccionario.copy()
copiaDic1 = dict(diccionario)
#Funcion de limpiado de diccionario
diccionario.clear()
print(copiaDic,copiaDic1)

panchito = {
    "nombre":"panchito",
    "edad": 7
}

fluffy = {
    "nombre": "fluffy",
    "edad": 6
}

#Diccionario de disccionario
gatitos = {
    "gato1":{
        "nombre": "robert",
        "edad":5
    },
    "gato2":{
        "nombre": "Black mamba",
        "edad": 6
    },
    "gato3": panchito,
    "gato4":fluffy
}
print(gatitos)
#Constructor dict nos ayuda a crear diccionarios
perritos = dict(nombre = "Chanchito feliz", edad = 6)

print(perritos)

#BOOLEANOS

verdadero = True
falso = False

print(verdadero,falso)