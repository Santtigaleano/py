'''alumnos=["Jorge","Pedro", "Raúl"]
'''
'''''
for i in alumnos:
    print("Hola")
    print(i)
'''

#ejemplo simple
'''
for a in alumnos:
    print("El nombre del alumno es: ", a)
'''
from pydoc import doc


Cantidad=0
Provincias= []

'''
Provincias.append (input ("Escribir una provincia"))
Provincias.append (input ("Escribir una provincia"))
Provincias.append(input ("Escribir una provincia"))
Provincias.append(input ("Escribir una provincia"))
''' 
'''
calor=0
frio=0
Provincias=["Buenos Aires", "Mendoza", "Rio negro", "Neuquen"]
for a in Provincias:
    Cantidad= Cantidad +1

for i in Provincias:    
    if i =="Mendoza" or i== "Buenos Aires":
        calor=calor+1
    else:
        frio=frio+1

print("Las ciudades que hace calor son:", calor)
print("Las ciudades que hace frio son:", frio)
        
        
print("La cantidad de Provincias es: ", Cantidad)
'''
'''
r_num=0
cuenta=[150,200,300,400,100]

for num in cuenta:
    r_num=num + r_num
    if r_num > 1000:
        print("Paga el profe")
    else:
        print("Pago yo")
print ("El total de la cuenta es", r_num)
'''
'''
palabra="PYTHON"

for i in "PYTHON":
    if i == "Y":
        continue  #Saltea #Break_Termina
    else:
        print(i)
'''
'''
for elemento in [1,2,3]:
    print(elemento)
for elemento in (1,2,3):
    print(elemento)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
'''
'''
for line in open(Yo.txt):
    print(line)
    input()
'''

