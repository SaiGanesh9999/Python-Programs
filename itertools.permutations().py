from itertools import permutations
s,n=input().split()
p=permutations(s,int(n))
p=sorted(list(p))
l=[''.join(list(i)) for i in p]
for i in l:
    print(i)
