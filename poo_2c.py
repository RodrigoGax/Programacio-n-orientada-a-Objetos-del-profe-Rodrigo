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
        return max(0,self.fuerza - enemigo.defensa)
    
    def atacar(self,enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = max(0,enemigo.vida - daño)
        print(self.nombre,"ha realizado",daño,"puntos de daño a", enemigo.nombre)
        print("Vida de",enemigo.nombre,"es",enemigo.vida)

class Guerrero(Personaje):
    
    #Sobreescribir el constructor
    def __init__(self,nombre,fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre,fuerza, inteligencia, defensa, vida)
        self.espada = espada
        
    #Sobrecribir impresión de atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Espada:",self.espada)
        
    #Sobrescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
    
    #Escoger navaja
    def escoger_navaja(self):
        opcion = int(input("Escoge la navaja de la muerte:\n(1) Navaja suiza, daño 10.\n(2) Navaja pioja, daño 6.\n>>>>>"))
        if(opcion == 1):
            self.espada = 10
        elif(opcion == 2):
            self.espada = 6
        else:
            print("Valor inválido, intente nuevamente")  
            #Vuelva a ejecutar el método escoger_navaja  
            self.escoger_navaja()

class Mago(Personaje):
    
    #Sobreescribir el constructor
    def __init__(self,nombre,fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre,fuerza, inteligencia, defensa, vida)
        self.libro = libro
        
    #Sobrecribir impresión de atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Libro:",self.libro)
        
    #Sobrescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
    
    #Escoger navaja
    def escoger_libro(self):
        opcion = int(input("Escoge el libro de la sabiduría:\n(1) El principito, daño 10.\n(2) Crepúsculo, daño 6.\n>>>>>"))
        if(opcion == 1):
            self.libro = 10
        elif(opcion == 2):
            self.libro = 6
        else:
            print("Valor inválido, intente nuevamente")  
            #Vuelva a ejecutar el método escoger_libro  
            self.escoger_libro()

#Crear todos objetos
persona = Personaje("Ángel Suárez", 20,15,10,100)
arturoSuarez = Guerrero("Arturo Suárez", 20, 15,10,100,5)
gandalf = Mago("Gandalf", 20, 15,10,100,5)
#Atributos antes de la tragedia
persona.imprimir_atributos()
arturoSuarez.imprimir_atributos()
gandalf.imprimir_atributos()
#Ataques sin piedad
persona.atacar(arturoSuarez)
arturoSuarez.atacar(gandalf)
gandalf.atacar(persona)
#Atributos después de la tragedia
persona.imprimir_atributos()
arturoSuarez.imprimir_atributos()
gandalf.imprimir_atributos()

#print("El valor de espada es: ", arturoSuarez.espada)

    
 
        
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
# mi_personaje.vida = 2

# print("El nombre de mi personaje es: ",mi_personaje.nombre)
# print("El fuerza de mi personaje es: ",mi_personaje.fuerza)
# print("El inteligencia de mi personaje es: ",mi_personaje.inteligencia)
# print("El defensa de mi personaje es: ",mi_personaje.defensa)
# print("El vida de mi personaje es: ",mi_personaje.vida)