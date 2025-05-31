a = int(input())
b = int(input())
k = int(input())

c = a / b
c = str(c)

pos_p = c.find('.')
ln = len(c[pos_p + 1:])

if(ln < k):
    c += '0' * (k - ln)
elif(ln > k):
    c = c[:pos_p] + c[pos_p:pos_p + k]

print(c)