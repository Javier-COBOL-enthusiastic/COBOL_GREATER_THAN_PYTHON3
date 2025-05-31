n = input().split()
x = int(n[0])
y = int(n[1])

if(x > 0 and y > 0):
    print("Peligro")
    exit()

sum = x ** 2 + y ** 2
if(sum <= 25):
    print("Peligro")
    exit()

print("Seguro")

