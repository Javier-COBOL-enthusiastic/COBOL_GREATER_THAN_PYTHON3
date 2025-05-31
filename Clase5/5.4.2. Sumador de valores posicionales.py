n = str(input())

while(len(n) > 1):
    n = list(map(lambda x : int(x), n))
    n = str(sum(n))
    print(n)