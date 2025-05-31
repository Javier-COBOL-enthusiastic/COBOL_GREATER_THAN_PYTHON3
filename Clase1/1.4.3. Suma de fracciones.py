def mcd(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    return a

def mcm(a, b):
    return a * b // mcd(a, b)


    


n = int(input())
fr = [input() for x in range(n)]
nume = [int(x[x.find('/') - 1])  for x in fr]
deno = [int(x[x.find('/') + 1]) for x in fr]

den = deno[0]
for d in deno[1:]:
    den = mcm(den, d)

num = 0
for x in range(len(deno)):
    num += nume[x] * (den // deno[x])
    
g = mcd(abs(num), den)
num //= g
den //= g

print(f"{num}/{den}") 
