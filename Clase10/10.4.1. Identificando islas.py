"""
4
5
1,1,0,1,1
0,1,0,0,0
0,0,1,1,1
1,0,0,0,1
"""

def elim_vec(tabla : list, cords : tuple):
    if(tabla[cords[0]][cords[1]] == "0"):
        return
        
    tabla[cords[0]][cords[1]] = "0"
    
    if(cords[0] > 0):
        elim_vec(tabla, (cords[0] - 1, cords[1]))
    if(cords[0] < len(tabla) - 1):
        elim_vec(tabla, (cords[0] + 1, cords[1]))
    if(cords[1] > 0):
        elim_vec(tabla, (cords[0], cords[1] - 1))
    if(cords[1] < len(tabla[0]) - 1):
        elim_vec(tabla, (cords[0], cords[1] + 1))    
    


n = int(input())
m = int(input())


matrix = [input() for c in range(n)]

matrix = list(map(lambda x : x.split(','), matrix))


n_isla = 0

for i in range(n):
    for j in range(m):
        if(matrix[i][j] == "1"):
            elim_vec(matrix, (i, j))
            n_isla += 1

print(n_isla)