from itertools import*
n=1
while 1:R=range(2**n);P=[[sum((x>>i&1)<<p[i]for i in p)for x in R]for p in permutations(R[:n])];print(len({min(tuple(a[t[y]]for y in b)for a in P for b in P)for t in permutations(R)}));n+=1
