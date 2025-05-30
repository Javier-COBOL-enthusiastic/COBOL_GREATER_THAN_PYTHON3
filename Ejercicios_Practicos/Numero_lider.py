a = input()
#1 65 1 1 16 5 6 8 6 4
c = [int(x) for x in a.split()]

nums = []

while(len(c) > 1):
    m_ = max(c)
    c = c[c.index(m_) + 1::]
    nums.append(m_)
    
print(nums)

    