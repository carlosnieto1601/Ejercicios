

# print("Programa de becas: ")

# distancia_escuela=int(input("Introduce la distancia a la escuelaa en km"))
# print(distancia_escuela)

# numero_hermanos=int(input("Introduce el N° de hermanos en el centro"))
# print(numero_hermanos)

# salario_familiar=int(input("Introduce salario presidente"))
# print(salario_familiar)


# if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
#     print("tiene derecho a beca")
# else:
#     print("no tiene derecho")

print("Asignatura: ")
print("asignatura operativas: ")
opcion=input("Escribe la asignatura")
asignatura=opcion.lower()
if asignatura in ("informatica", "sociales", "ingles"):
    print("asignatura elegido" + asignatura)
else:
    print("la asignatura no esta contemplada")