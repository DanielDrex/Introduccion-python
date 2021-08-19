#************************************************************************************

# FUNCIONES:

#Uso de la palabra reservada def

def miFuncion():
    print('Mi primera funcion')

miFuncion() # Se manda llamar a nuestra funcion

#Funcion con argumentos
def imprimeDato(arg1,arg2,arg3):
    print(arg1,arg2,arg3)

imprimeDato('parametro 1','parametro 2','parametro 3')

def imprimeNombre(nombre, apellido):
    print('El nombre completo es:',nombre,apellido)

imprimeNombre('Pedro','Montes')

#Funcion con argumentos variables
def imprimeNombres(*nombres):
    print('Los nombres son',nombres) #Impresion de todos los nombres
    print('Un solo nombre es',nombres[2])

imprimeNombres('juan','carlos','maria','marco')

#Funcion con llamada que contiene parametros en otro orden que los argumentos de la funcion
def impNombre (apellido,nombre):
    print(nombre,apellido)
#Hacemos uso de la llave o nombre del argumento de la funcion para poder indicarlo aunque en la llamada se tengan en distinto orden que en la funcion
impNombre(nombre = 'juan',apellido = 'perez') # Aqui indicamos el nombre y apellido y lo pasamos a la funcion aunque lleven un orden diferente

#Otra sintaxis para indicar los parametros, uso de argumentos como si fuera diccionario
#Se hace uso de el doble asterisco ** para indicar el parametro
def impNombre2 (**kwargs):
    print(kwargs['nombre'],kwargs['apellido'])

impNombre2(nombre = 'Juan',apellido = 'perez')

#Estas dos ultimas funciones tienen el mismo comportamiento en la impresion pera la forma de acceder al parametro es diferente



