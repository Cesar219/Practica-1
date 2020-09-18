#Punto 1
#Clase 1
class audi:
    def __init__(self):
        self.marca = audi
        self.cantidad_ruedas = 4
        self.cantidad_puertas = 4
        self.tipo_combustible = "diesel"
        self.cantidad_combustible = 12


#Clase 2
class headphones():
    def __init__(self):
        self.marca = "hellcrack"
        self.lucesled_voltaje = 5
        self.tipo_audio = "hd"

#clase 3
class control():
    def __init__(self):
        self.marca = "etpark"
        self.color = "negro"
        self.pin_carga = "usb"


#Punto 2
class Estudiante:
    promedio = 0

    def __init__(self, promedio):
        self.promedio = promedio

    def valor_promedio(self):
        grade = []
        x = 0
        self.promedio = 0
        sum = 0
        while x < 4:
            grades = int(input("Write grade: "))
            x += 1
            grade.append(grades)
            for i in grade:
                sum += i
                self.promedio += 1
        promedio = sum / self.promedio
        if promedio > 100:
            print("Promedio invalida!")
        print("Tu promedio: ",promedio)



#Punto 3
class Arithmetica:

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b


#Punto 4
class personaje:
    def mover_arriba(self):
        pass

    def mover_abajo(self):
        pass

    def mover_derecha(self):
        pass

    def mover_izquierda(self):
        pass


class Mario(personaje):
    personaje = personaje()
    personaje.mover_arriba()
    personaje.mover_abajo()
    personaje.mover_derecha()
    personaje.mover_izquierda()


class Koopa(personaje):
    personaje = personaje()
    personaje.mover_arriba()
    personaje.mover_abajo()
    personaje.mover_derecha()
    personaje.mover_izquierda()


#Punto 5 
class Carro:
    def __init__(self):

        self.cantidad_combustible = 12
        self.acelerador = 1
        self.motor = "apagado"
        


    def Encender(self):
        if self.motor == "apagado":
            self.motor = int(input("Ingrese 5 para encender el motor: "))
            if self.motor == 5:
                print("Motor encendido")
                if self.motor == 5:
                    self.acelerador = int(input("ingrese 1 para acelerar: "))
                    while self.acelerador == 1:
                        while self.cantidad_combustible > 0:
                            print("Pisando acelerador.")
                            print("Acelerando")
                            self.cantidad_combustible = self.cantidad_combustible - 1
                            print(f"El galon va por:{self.cantidad_combustible} Galones.")
                            self.acelerador = int(input("Desea dejar de acelerar?presione 0: " ))
                            while self.acelerador == 0:
                                print("Usted a dejado de acelerar.")
                                self.acelerador = int(input("ingrese 1 para acelerar: "))
                        
                                while self.cantidad_combustible < 1:

                                    print("No hay galones insuficientes para acelerar")
                                    self.cantidad_combustible = int(input("Ingrese 5 para rellenar los galones: "))
                                    self.acelerador = int(input("ingrese 1 para acelerar: "))

audi = Carro()
audi.Encender()