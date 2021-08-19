#lOOP WHILE
i = 0
#Break nos ayuda a interrumpir el ciclo siempre y cuando se cumpla la condicion
while i < 5:
    print(i)
    if i == 3:
        break
    i+=1

i = 0
while i < 5:
    i+=1
    if i == 3:
        continue #El continue salta la instruccion siguiente
    print(i)

#LOOP FOR

#Recorrido de una lista
usuarios = ['chanchito feliz','felipe','roberto','nicolas']

for usuario in usuarios:
    print(usuario)

#Recorrido de caracteres de un String
usuario1 = 'Usuario 1'

for c in usuario1:
    print(c)

#Uso de break en loop for
for usuario in usuarios:
    if usuario == 'roberto':
        print(usuario) #Imprimer el usuario si se cumple la condicion
        break # Rompe el ciclo y se termina la iteracion

#Uso de continue en loop for
for usuario in usuarios:
    if usuario == 'roberto':
        continue # Si se cumple la condicion, NO se imprimira el usuario de la condicion
    print(usuario)

#Rangos 
#Rango sin valor inicial especifico, en este caso por defecto es 0
for x in range(6):
    print(x)

#Rango con valor inicial
for x in range(2,20):
    print(x)

#Rango con valor inicial y salto especifico, con una condicion else en caso de que el loop finalize
for x in range(1,20,5):
    print(x)
else:
    print('Se acabo el ciclo')

#loops FOR anidados 
#Hacemos uso de la lista de usuarios y la lista de edades

usuarios = ['chanchito feliz','felipe','roberto','nicolas']
edades = [24,25,26,30]

for usuario in usuarios:
    for edad in edades:
        print(usuario,edad)

