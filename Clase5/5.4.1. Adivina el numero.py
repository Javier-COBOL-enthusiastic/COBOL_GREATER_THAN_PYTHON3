import random

n = random.randrange(1, 100)
a = int(input())
while(a != n):
    if(a > n):
        print("El numero secreto es menor")
    else:   
        print("El numero secreto es mayor")
    a = int(input())

print("Has adivinado el numero secreto")