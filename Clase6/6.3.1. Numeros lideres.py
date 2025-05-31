a = input()
#1 65 1 1 65 16 5 6 8 6 4
c = [int(x) for x in a.split()][::-1]
    
max_d = c.pop(0)

l = []
for num in c:       
    if(num > max_d):
        l.append(num)
        max_d = num

print(l[::-1])