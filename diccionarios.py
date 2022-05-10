## estructuras de datos que no permite alamcenar valores
#clave : valor se le asigna una clave unica

midiccionario={"alemania":"berlin","francia":"paris"}
midiccionario["italia"]="lisboa" # asignar un nuevo valor
print(midiccionario)
midiccionario["italia"]="roma" #modificar el valor de la clave se modifica
print(midiccionario["alemania"])
del midiccionario["alemania"] #eliminar
print(midiccionario)

diccionario= {"carlos":"nombre", 23:"teo", "capital":10}
print(diccionario)

mitupla=["madrid", "barcelona","alemani"]
dicc={mitupla[0]:"colombia", mitupla[1]:"col",mitupla[2]:"col"}
print(dicc)

diccio={23:"jordan", "nombre":"carlos", "equipo":"junior", "anillos":{"temporadas":[1998,1991,1992,1992,1993]}}
print(diccio.keys())# imprime las claves que pertencen al diccio
print(diccio.values())# imprime los valores de la claves
print(len(diccio))# imprime la longitud
print(diccio["anillos"])

