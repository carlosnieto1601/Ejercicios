# son estructuras que extraen valores de una funcion y se almacenan en objetos

def generaPares(limite):
    num=1
    milista=[]
    while num<limite:
        milista.append(num*2)
        num=num+1
    return milista


print(generaPares(10))

def generaPares(limite):
    num=1
    milista=[]
    while num<limite:
        yield num*2
        num=num+1

devuelvepares=generaPares(10)

for i in devuelvepares:
    print(i)

def generaPares(limite):
    num1=1
    while num1<limite:
        yield num1*2 
        num1=num1+1

devuelvepares=generaPares(10)

print(next(devuelvepares))
print("aqui podria ir mas codigo")

print(next(devuelvepares))
print("aqui podria ir mas codigo")

print(next(devuelvepares))


