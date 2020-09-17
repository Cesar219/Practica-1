#Punto 1

print("Bienvenido a la calculadora de potencias")


x = int(input("Ingrese su cantidad base (x): "))
y = int(input("Ingrese su cantidad de potencia (y): "))

def potencia():
    resultado = x ** y
    print(f"{x}^{y} = {resultado}")

potencia()

print("Gracias por usar nuestra calculadora")


#Punto 2

numero = int(input("Ingrese su numero del 1 al 10: "))

def escrito():
    
    if numero == 1:
        print("Uno")
    elif numero == 2:
        print("Dos")
    elif numero == 3:
        print("Tres")
    elif numero == 4:
        print("Cuatro")
    elif numero == 5:
        print("Cinco")
    elif numero == 6:
        print("Seis")
    elif numero == 7:
        print("Siete")
    elif numero == 8:
        print("Ocho")
    elif numero == 9:
        print("Nueve")
    elif numero == 10:
        print("Diez")
    else:
        print("Su numero esta fuera del listado")


escrito()

#Punto 3

y = int(input("Introduzca el año: "))

def bisiesto(año):
    prueba = año % 4
    if prueba == 0:
        print(f"{año} Este año si es bisiesto")
    else:
        print(f"{año} Este año no es bisiesto")


bisiesto(y)

#Punto 4

n1 = input("Ingrese su primer numero: ")

n2 = input("Ingrese su segundo numero: ")

def igual():
    return n1 == n2

res = igual()
print(res)

#Punto 5

def isPalindrome(numero):
    if str(numero)==str(numero)[::-1]:
        return True
    else:
        return False
maxPalindrome = 1
for numero1 in range(100,999):
    for numero2 in range(100,999):
        producto = numero1*numero2  
        if isPalindrome(producto):
            if producto>maxPalindrome:
                maxPalindrome = producto
                maxnum1 = numero1
                maxnum2 = numero2
print (maxPalindrome,"=",maxnum1,"x",maxnum2)

#Punto 6

cedula = input("Introduzca su cedula de identidad: ")

def identidad(ced):
     
     if len(cedula) == 11:
         print("Su cedula es valida")
         return True
     else:
         print("Su cedula no es valida")


identidad(cedula)

#Punto 7

def duplicar(c,d,e):

    return [c*2, d*2, e*2]

print("Ingrese los numeros a la lista, para empezar a duplicarlos ")
z= int(input("> "))
w= int(input("> "))
x= int(input("> "))

res = duplicar(z,w,x)
print(res)

#Punto 8
def pr(a,b):
    while a <= b:
        res = 6 * a
        print (f"{6} X {a} = {res}")
        a += 1

print("Bienvenido a la calculadora")

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero mayor que el anterior: "))

if n1 > n2:
    print(f"{n2} no es mayor que {n1}, intentelo de nuevo ")

else:
    pr(n1,n2) 
