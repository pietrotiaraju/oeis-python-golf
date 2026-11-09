from itertools import*
n=1
while 1:R=range(2**n);P=[[s^sum((x>>i&1)<<p[i]for i in p)for x in R]for p in permutations(R[:n])for s in R];print(len({min(tuple(a[t[y]]for y in b)for a in P for b in P[::2**n])for t in permutations(R)if t[0]<1}));n+=1
