a = input()
b = input()
l_b = len(b)
l_a = len(a)

if(l_b > l_a):
    a = a.zfill(l_b)
elif(l_b < l_a):
    b = b.zfill(l_a)

sum = ""
l = 0
for x in range(l_a - 1, -1, -1):
    n = int(a[x]) + int(b[x]) + l
    sum += (str(n % 10))
    l = n // 10

if(l):
    sum += l

print(sum[::-1])