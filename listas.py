#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
temperaturas= [12,20,51,14,15,412,23.2, True]
print(temperaturas)
print (type(temperaturas))
print (len(temperaturas))
##ver elementos de una lista
temperaturas[6]=90
print(temperaturas[6])

##AGREGAR ELEMENTO A UNA LISTA
temperaturas.append(31.5)
print(temperaturas)
print(temperaturas[8])
salir= "n"
''''''
temperaturas= []
sumas_de_temperaturas=0
salir="n"

while salir== "n":
	temperaturas=float(input("ingrese temperatura"))
	temperaturas.append(1)
	input("quiere salir s/n")
	sumas_de_temperaturas=sumas_de_temperaturas+temperaturas
	
	
print(temperaturas)
print(sumas_de_temperaturas/len(temperaturas))
 ''''''
listaprueba=["Carlos",10,True]
listaprueba.append(2)
listaprueba.insert(8,"Jorge")
print(listaprueba)
del listaprueba[1]
print(listaprueba)
numero_aleatorio=float
print(listaprueba[len(temperaturas)
''''''
##RECORRER UNA LISTA

'''
temperaturas= [15,20,16,12,23,32,53]   

''''
indice=0

while indice < len(temperaturas):
	if indice==0:
		print("El lunes la temperatura fue de: _",temperaturas[indice])
	elif indice==1:
		print("El martes la temperatura fue de: _", temperaturas[indice])
	elif indice==1:
		print("El miercoles la temperatura fue de:_", mperaturas[indice])
	elif indice==1:
		print("El martes la temperatura fue de: _", temperaturas[indice])
	elif indice==1:
		print("El martes la temperatura fue de: _", temperaturas[indice])
	elif indice==1:
		print("El martes la temperatura fue de: _", temperaturas[indice])
	elif indice==1:
		print("El martes la temperatura fue de: _", temperaturas[indice])
	
'''
'''
temperatiras.pop() #borro elemento final
temperaturas.remove(20) o sino [1] #orrar elemento
'''
temperaturas.remove[1]
temperaturas.sort()
print(temperaturas)

