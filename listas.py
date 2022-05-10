
lista=["hola", 2,3,True]
lista.append("sandra") # agraga campo al final de la lista
lista.insert(0,"carlos") #inserta en la posicion que querramos
lista.extend([1,2,2,2,5,6]) # inserta y concatena al final de la lista
lista.remove("carlos") #elimina 
lista.pop()# elimina el ultimo de la lista
print(lista[:]) #muestra a lista completa
print(lista.index("hola")) #muesta la posicion del elemento
# busca si existe el campo y devuelve true o false
print("ccarlos" in lista)


