class Personaje:
    #Atributos de la clase
    # nombre = 'Default'
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    #¿Qué es self? Es una referencia al mismo objeto
    #¿Qué es el método init? Constructor que inicializa
    #atributos de un objeto
    #¿Por qué se usa doble guión bajo? Dunder. Porque es
    #método mágico.
    #¿Cuándo se ejecuta el método init? Autom. al crear
    #una nueva instancia
    
    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza:",self.fuerza)
        print("-Inteligencia:",self.inteligencia)
        print("-Defensa:",self.defensa)
        print("-Vida:",self.vida)
    
    def subir_nivel(self,fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    
    def esta_vivo(self):        
        return self.vida > 0
        
    def morir(self):
        self.vida = 0
        print(self.nombre,"ha muerto")
        
    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self,enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre,"ha realizado",daño,"puntos de daño a", enemigo.nombre)
        print("Vida de",enemigo.nombre,"es",enemigo.vida)

class Guerrero(Personaje):
    
    #Sobreescribir el constructor
    def __init__(self,nombre,fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre,fuerza, inteligencia, defensa, vida)
        self.espada = espada

arturoSuarez = Guerrero("Arturo Suárez", 12, 3000,2,100,.5)
arturoSuarez.imprimir_atributos()
print("El valor de espada es: ", arturoSuarez.espada)

    
 
        
#Variable del constructor 
# mi_personaje = Personaje("EsteBandido", 100, 50, 45, 100)
# mi_enemigo = Personaje("Ángel",70,100,70,100)
# mi_personaje.imprimir_atributos()
# mi_personaje.atacar(mi_enemigo)
# mi_personaje.morir()
#print(mi_personaje.esta_vivo())
# mi_personaje.subir_nivel(15,5,10)
# print("Valores actualizados")
# mi_personaje.imprimir_atributos()

#Modificando valores de los atributos
# mi_personaje.nombre = "EstebanDido"
# mi_personaje.fuerza = 300
# mi_personaje.inteligencia = -2
# mi_personaje.defensa = 30
# mi_pers