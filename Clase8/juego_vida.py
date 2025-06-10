import pygame

pygame.init()

screen = pygame.display.set_mode((1020, 300))
clock = pygame.time.Clock()



tabla = []
with open("genesis.txt", "r", newline="") as file:
    for line in file:
        tabla.append([c for c in line.strip()])


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
    for y in range(ylower, yupper, 1):
        for x in range(xlower, xupper, 1):
            box.append(tabla[y][x])
    return box.count("1") - 1

run = True

cuadros = [] 
for y in range(len(tabla)):
    cuadros.append([])
    for x in range(len(tabla[0])):
        cuadros[y].append(pygame.Rect(0 + (15 * x), 0 + (15 * y), 15, 15))

print(count(tabla, (6, 34)))

while(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill("white")
    
    for y in range(len(tabla)):
        for x in range(len(tabla[0])):            
            match tabla[y][x]:
                case "0":
                    if(count(tabla, (y, x)) == 2): #2 pq si fueran 3 - 1 == 2
                        tabla[y][x] = "1"
                    pygame.draw.rect(screen, (0, 0, 255), cuadros[y][x])
                case "1":
                    n = count(tabla, (y, x))                    
                    if(n > 3 or n <= 1):
                        tabla[y][x] = "0"
                    pygame.draw.rect(screen, (0,255,0), cuadros[y][x])
        
    pygame.display.flip()
    clock.tick(1)  
                            
pygame.quit()
