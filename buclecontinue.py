
for letra in "python":
    if letra=="h":
        continue
    print("viendo la letra" + letra)

nombre= "pildoras informaticas"
print(len(nombre))


nombre= "pildoras informaticas"
contador=0
for i in nombre:
    if i==" ":
        continue
    contador+=1
print(contador)



email=input("Introduce tu email, por favor: ")
for i in email:
    if i=="@":
        arroba=True
        break;
else:
    arroba=False

print(arroba)