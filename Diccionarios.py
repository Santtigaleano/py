#En las tuplas no se pueden reemplazar valor

#Diccionarios
'''
temperatura=[10,23,17,33]
diccionario= {123:"Carlos", 456:"Jose", 789:"Juan","temp": temperatura}
print(diccionario[123])

print([temperatura])

diccionario[999]="Raul"

print(diccionario)

#en los diccionarios no hay posiciones 
#no se puede usar append
#No se puede repetir claves

for laquequiera in diccionario:
    print(laquequiera)
'''

#lista para ciclar que se hace sola

#lista=[1,2,3,4,5]



###imprimir numeros en rango, siempre empieza desde el cero
'''
range(1,22)
for numero in range (1,22):
    print(numero)
'''
'''''
range(64,74)
suma=0

for numero in range(64,75):
    suma= numero+numero
    print(numero)
    print(suma)
'''
###range pero de 2 en 2
'''
for i in range (600,800,9):
    print(i)
'''

###cuenta regresiva
'''
for numero in range (10,0,-1):
    print(numero)
'''

##si no me interesa el contador pero quiero hacer que el for cicle
'''
for _ in range(5):
    print("hola mundo")
'''

###bucle anidado
'''
suma_total=0

for i in range(5):
    print ("Valor de i:", i)
    suma_total= suma_total +1
    for j in range(3):
        print("valor de j:",j)
    suma_total= j+suma_total
    print(suma_total)

print(suma_total)
''

inicio= int(input("Ingrese el numero de inicio del rango: "))
final= int(input("Ingrese el numero de fin del rango:"))
multiplos=[]
multiplos_de_tres=[]
multiplos_de_cinco=[]
no_multiplos=[]
for n in range (inicio, final + 1):
    if n%3 == 0 and n%5 == 0:
        multiplos.append(n)
    elif n%3==0:
        multiplos_de_tres.append(n)
    elif n%5 == 0:
            multiplos_de_cinco.append(n)
    else:
        no_multiplos.append(n)
print("Los multiplos de 3 y 5 en ese rango son: ", multiplos)
print("Los multiplos de 3 son: ", multiplos_de_tres)
print("los multiplos de 5 son: ", multiplos_de_cinco)
print("Los que no son multiplos son: ", no_multiplos)
'''

