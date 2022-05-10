


from inspect import classify_class_attrs


valido=False

email= input("introduce tu email:")
for i in range(len(email)):
    if email[i]=="@":
        valido=True
if valido:
    print("Email Correcto")
else:
    print("email incorrecto")
