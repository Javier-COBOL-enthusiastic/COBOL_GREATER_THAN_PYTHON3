"""
4
5
1,0,1,1,1
0,1,0,0,0
0,0,1,0,1
1,1,0,0,0
"""


def count(tabla : list, cords : tuple):
    box = []

    ylower = cords[0] - 1    
    if(ylower < 0):
        ylower = 0


    yupper = cords[0] + 2
    if(yupper > len(tabla)):
        yupper = len(tabla)

    xlower = cords[1] - 1
    if(xlower < 0):
        xlower = 0

    xupper = cords[1] + 2
    if(xupper > len(tabla[0])):
        xupper = len(tabla[0])


    #print(f"{cords[0]}, {cords[1]}; {xlower}->{xupper}, {ylower}->{yupper}; {len(tabla)}x{len(tabla[0])}")
    for i in range(ylower, yupper, 1):
        for j in range(xlower, xupper, 1):
            if(i == cords[0] and j == cords[1]):
                box.append("0")
            else:
                box.append(tabla[i][j])
    return box.count("1")

n = int(input())
m = int(input())


matrix = [input() for c in range(n)]

matrix = list(map(lambda x : x.split(','), matrix))

ans = [[] for c in range(n)]

for i in range(n):
    for j in range(m):
        ans[i].append(count(matrix, (i, j)))

print(ans)