from gettext import dgettext
from smtplib import LMTP


email=False
# for i in ["pildoras", "Infomaticas", 3]:
#     print("hola", end="  ")
miemail=input("introduce email")
for i in miemail:
    if(i=="@"):
        email=True

if email==True:
    print("Email es correcto")
else:
    print("El email no es correcto")


for i in range(5): # nos devuelve un tipo array 
    print("hola")


for i in range(5,50,3): # f 
    print(f"valor de la variable {i}")
