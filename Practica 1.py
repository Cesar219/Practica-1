#Punto 1
print(type(4 < 2))

#Punto 2
nombre = input("ingrese su nombre: ")
print("Bienvenido : " + nombre)

#Punto 3
numero = input("ingrese su numero: ")
ope = int(numero) % 2
if ope == 0:
    print(numero + " es par")
else:
    print(numero + " es impar")

    
#Punto 4
a = 3
c = 9
if a > c :
    print ("Su resultado es verdadero")
else:
    print("Su resultado es falso")

#Punto 5
dolar = input("Ingrese la cantidad de dolar: ")
dolar = float(dolar)
valor = 58.45
print(dolar * valor)

#Punto 6
celsius = input("ingrese su grado celsius: ")
celsius = float(celsius)
farenheit = 9/5
print(celsius * farenheit + 32)

#Punto 7
nota1 = 90
nota2 = 95
nota3 = 77
nota4 = 92
suma = nota1 + nota2 +nota3 + nota4
promedio = suma / 4
if promedio <= 60: 
    print("calificacion : F")
elif promedio <= 70:
    print("calificacion : D")
elif promedio <= 80:
    print("calificacion : C")
elif promedio <= 90:
    print("calificacion : B")
else:
    print("calificacion : A")


#Punto 8
monto = input("introduzca monto: ")
monto = float(monto)
cuotas = input("introduzca cantidad de cuotas: ")
cuotas = int(cuotas)
interes = input("introduzca el porcentaje de interes: ")
interes = float(interes)
in1 = (1+ interes) ** cuotas
in2 = ( interes * in1) / (in1 - 1)
resultado = monto * in2
print(resultado)
