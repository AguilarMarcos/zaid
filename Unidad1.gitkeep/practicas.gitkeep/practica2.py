#practica2: clases,objetos,atributos y metodos
class persona:
    #c0nstructor de la clase
    def __init__(self,nombre,apellido,edad):
        #creacion de atributos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        #doble guion bajo es privado
        self.__cuenta = None

    def asignar_cuenta(self,cuenta):
        self.__cuenta =  cuenta
        print(f"{self.nombre} ahora tiene una cuenta bancaria")

    def consultar_saldo(self):
        if self.__cuenta:
            print(f"el saldo de {self.nombre} es: ${self.__cuenta.mostrar_saldo()}") #saldo
        else:
            print(f"{self.nombre} no tiene una cuenta creada")   

    def presentarse(self):
        print(f"Hola mi nombre es: {self.nombre}, mi apellido es {self.apellido}, y tengo {self.edad} años")

    def cumplir_años(self):
        self.edad += 1
        print("esta persona cumplio: {self.edad} años")

class cuenta_bancaria:
        def __init__(self,num_cuenta,saldo):
            self.num_cuenta = num_cuenta
            self.__saldo = saldo #datos/atributo privado

        def mostrar_saldo(self):
            return self.__saldo

        def depositar(self,cantidad):
            if cantidad > 0:
                self.__saldo += cantidad
                print(f"se deposito la cantidad de $ {cantidad} a la cuenta")
            else:
                print("ingersa una cantidad valida")

        def retirar(self,cantidad):
            if 0 < cantidad <= self.__saldo:
                self.__saldo -= cantidad 
                print(f"se retiro la cantidad de {cantidad}, nuevo saldo: {self.__saldo}")
            else:
                print("saldo insuficiente")            
            

   #creacion del objeto o instancia de un objeto
estudiante1 = persona("estrada","hernandez", 40)
cuenta1 = cuenta_bancaria("001",500)
estudiante1.asignar_cuenta(cuenta1)
estudiante1.consultar_saldo()



cuenta1.depositar(200)
cuenta1.retirar(100)



estudiante2 = persona("jimenez","vasquez")

estudiante1.presentarse()
estudiante2.presentarse()

estudiante1.cumplir_años()


class Coche:
    # Constructor de la clase
    def __init__(self, marca, precio, color):
        # Creación de atributos
        self.marca = marca
        self.precio = precio
        self.color = color

    # Método para mostrar las características del coche
    def caracteristicas(self):
        print(f"La marca del coche es: {self.marca}, este coche vale {self.precio}, y su color es {self.color}")

    # Método para confirmar la marca del coche
    def tu_coche(self):
        print(f"Este es tu coche: {self.marca}")

    # Método para verificar el color del coche
    def afirmacion(self):
        print(f"¿Estás seguro de tu color: {self.color}?")

# Creación de objetos (instancias de la clase Coche)
coche1 = Coche("Toyota", 25000, "Rojo")
coche2 = Coche("Honda", 30000, "Azul")

# Llamada a los métodos
coche1.caracteristicas()
coche1.tu_coche()
coche1.afirmacion()

coche2.caracteristicas()
coche2.tu_coche()
coche2.afirmacion()