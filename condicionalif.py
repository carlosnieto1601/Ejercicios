#

print("programa de evaluacion")
nota_alumno=input()

def evaluacion(nota):
    valoracion="aprobado"
    if nota < 5:
        valoracion="suspenso"
        calificacion=7
    return valoracion

print(evaluacion(int(nota_alumno)))

salario_presidente=int(input("Introduce salario presidente"))
print("Salario presidente: " + str(salario_presidente))

salario_director=int(input("Introduce salario presidente"))
print("Salario presidente: " + str(salario_director))

salario_jefe_area=int(input("Introduce salario presidente"))
print("Salario presidente: " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce salario presidente"))
print("Salario presidente: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("todo funciona")
else:
    print("Algo falla en esta empresa")
