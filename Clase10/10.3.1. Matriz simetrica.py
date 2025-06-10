"""
3
1,2,3
2,5,0
3,0,5


4
1,2,0,4
2,3,2,1
3,2,7,8
4,1,6,5
"""

n = int(input())

matrix = []

for i in range(n):
    d = input().split(',')
    matrix.append(list(map(lambda x : int(x), d)))

der = []
izq = []
for i in range(n):
    for c in matrix[i][:i]:
        izq.append(c)
    for c in matrix[i][i + 1:]:
        der.append(c)

for n in range(len(der)):
    if(der[n] != izq[n]):
        print("La matriz no es simetrica")
        exit()

print("La matriz es simetrica")