   #tuplas son listas inmutables,es decir que no se pueden modificar 
   #despues de su creacion

mitupla=("carlos",16,1,1996)
print(mitupla[2])

## metodo list para cambiar una tuplas en un lista 

milista=list(mitupla)
print(milista)

## metodo list para cambiar una listas en un tuplas 
lista=["juan", 1,2]
tupla=tuple(lista)
print(tupla)

print("juan" in tupla)

print(tupla.count(1))

# desempaquetado de tupla permite asignar a valor a diferentes variable

tuplas=("carlos", 16 , 1 , 1996)
nombre, dia, mes, agno = tuplas

print(nombre)
print(mes)
print(agno)
print(dia)
