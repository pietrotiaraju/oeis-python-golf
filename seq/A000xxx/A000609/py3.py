import math
n=0
while 1:
 R=range(2**n);V=[[0]];exec('V=[v+[a+c for a in v]for v in V for c in range(math.isqrt((n+1)**-~n)+2**n>>n)];'*n)
 print(len({tuple(f[p^s]for p in R)for f in{(*map(t.__lt__,v),)for v in V for t in v+[-1]}for s in R}));n+=1
