from itertools import*
n=0;C=combinations
while 1:R=range(n);print(len({min(sum(1<<p[a]*n+p[b]for a,b in P)for p in permutations(R))for k in range(1<<n)for P in C(C(R,2),k)if{(a,c)for a,b in P for x,c in P if b==x}<={*P}}));n+=1
