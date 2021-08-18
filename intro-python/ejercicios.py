'''
dato = input('ingrese dato: ')

lista = ['hola','mundo','chanchito','feliz','dragones']

if lista.count(dato) > 0:
    print('El dato existe:',dato)
else:
    print('El dato no existe:',dato)
'''

#Calculadora

primero = input('Ingrese primer numero: ')
try:
    primero = int(primero)
except:
    primero = 'chanchito feliz'

if primero == 'chanchito feliz':
    print('El valor ingresado no es un numero entero')
    exit()

segundo = input('Ingrese segundo numero: ')
try:
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('El valor ingresado no es un numero entero')
    exit()

simbolo = input('ingrese operacion: ')
if simbolo == '+':
    print('La suma de los dos numeros es:',primero+segundo)
elif simbolo == '-':
    print('La resta de los dos numeros es: ',primero-segundo)
elif simbolo == '*':
    print('La resta de los dos numeros es: ',primero*segundo)
elif simbolo == '/':
    print('La resta de los dos numeros es: ',primero/segundo)
else:
    print('El simbolo ingresado no es valido')

