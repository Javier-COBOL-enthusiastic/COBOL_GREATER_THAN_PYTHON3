"""
4
1 ,2 ,3 ,4
5 ,6 ,7 ,8
9 ,10,11,12
13,14,15,16
"""

n = int(input())

matrix = [input() for c in range(n)]

matrix = list(map(lambda x : x.split(','), matrix))

prin = []
sec = []

for i in range(n):
    prin.append(matrix[i][i])
    sec.append(matrix[i][(n - 1) - i])

print(prin)
print(sec)