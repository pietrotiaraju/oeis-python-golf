from itertools import*
n=0;C=combinations
while 1:R=range(n);r=range(1<<n);print(len({min(sum(1<<p[a]*n+p[b]for a,b in P)for p in permutations(R))for k in r for P in C(C(R,2),k)if{(a,c)for a,b in P for x,c in P if b==x}<={*P}and sum(all(s>>a&1==s>>b&1for a,b in P)for s in r)<3}));n+=1
