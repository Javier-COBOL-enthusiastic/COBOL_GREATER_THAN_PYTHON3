n = int(input())
if(n % 4 != 0):
    print("No bisiesto")
    exit()

if(n % 100 == 0 and n % 400 != 0):
    print("No bisiesto")
    exit()
    
print("Bisiesto")    








