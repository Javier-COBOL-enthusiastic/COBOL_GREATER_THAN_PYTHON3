#8 16 65 1 1 1 4 5 6 6
#8 16 65 13 2 1 4 5 6 2
#1, 2 .., n - 1, 0

def valid(a : list) -> bool:
    for x in range(len(a) - 1):        
        if(a[x] > a[x + 1]):
            return False
    return True

def rotate(a : list) -> list:
    temp = a[0]
    for x in range(len(a) - 1):
        a[x] = a[x + 1]
    a[-1] = temp    
    return a

a = input()
d = list(map(lambda x : int(x), a.split())) 

n = 0
while(not(valid(d)) and n < len(d)):            
    n += 1
    d = rotate(d)    

if(n == len(d)):
    n = -1
print(n)

