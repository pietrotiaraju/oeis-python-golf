import math
n=0
while 1:V=Q=[[0]];exec('V=[v+[a+c for a in v]for v in V for c in range(v[len(v)//2],math.isqrt((n+1)**-~n)+2**n>>n)];Q=[q+[a+c for a in q]for q in Q for c in{1<<i for i in range(n)}-{*q}];'*n);print(len({(*map(f.__getitem__,q),)for f in{(*map(t.__lt__,v),)for v in V for t in v+[-1]}if f[::2]!=f[1::2]if{*map(sum,zip(f,f[::-1]))}-{1}=={2}for q in Q}));n+=1
