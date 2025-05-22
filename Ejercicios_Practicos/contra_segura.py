contr = input()
if(len(contr) < 8):
    print("Contraseña no segura")
num = False
mayus = False
for c in contr:
    if(c.isdigit()):
        num = True
    if(c.isupper()):
        mayus = True

if(num and mayus):
    print("Contraseña segura")

else:
    print("Contraseña no segura")
