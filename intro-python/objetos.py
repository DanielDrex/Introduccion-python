#Las clases siempre inician con letra Mayuscula
class Usuario:
    nombre = 'Carlos'
    apellido = 'Feliz'

#Instancia de la clase usuario
usuario = Usuario()

#print(usuario.nombre,usuario.apellido)


#Clase Usuario2 con init (init se podria considerar como el constructor de clase)
class Usuario2:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

usuario2 = Usuario2('Juan','Perez')
usuario3 = Usuario2('Pedro','Flores')

print(usuario2.nombre,usuario2.apellido,usuario3.nombre,usuario3.apellido)
