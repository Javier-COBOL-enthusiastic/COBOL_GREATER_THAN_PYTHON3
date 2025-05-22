inm = input().split()

A = int(inm[0])
B = int(inm[1])
p = int(inm[2])
dst_a =  abs(A - p)
dst_b = abs(B - p)

if(dst_a == dst_b):
    print("Elevador A")
    exit()

if(dst_a > dst_b):
    print("Elevador B")    
else:
    print("Elevador A")