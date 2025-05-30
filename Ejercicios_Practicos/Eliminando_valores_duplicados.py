#1 8 1 1 6 5 6 8 8 4

a = input()
b = list(map(lambda x : int(x), a.split()))
vec = set(b)

d = []

for x in vec:
    d.append(b.index(x))

d.sort()
for x in d:
    print(b[x], end=" ")


    
