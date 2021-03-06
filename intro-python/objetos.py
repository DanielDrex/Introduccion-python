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
    
    def saludo(self):
        print('Hola mi nombre es',self.nombre,self.apellido)

usuario2 = Usuario2('Juan','Perez')
usuario3 = Usuario2('Pedro','Flores')

#Hacemos uso de nuestra funcion saludo
usuario2.saludo()
usuario3.saludo()

#Con la palabra reservada del podemos eliminar propiedades y/o objetos
'''
del usuario3.nombre
usuario3.saludo()
'''
#Herencia
class Admin(Usuario2):
    def superSaludo(self):
        print('Hola me llamo',self.nombre, 'y soy administrador')

admin = Admin('Super','Administrador')
admin.saludo()
admin.superSaludo()

class Animal:
    def __init__(self,nombre,onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
        
    def saludo(self):
        print('Hola, soy un',self.tipo, 'y mi nombre es',self.nombre,'y mi sonido es el',self.onomatopeya)


class Gato(Animal):
    tipo = 'gato'

class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('constructor extendido')
    
       
        
gato = Gato('lalo','maullido')
gato.saludo()
perro = Perro('robert','ladrido')
perro.saludo()