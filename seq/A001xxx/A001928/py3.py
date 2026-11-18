from itertools import*
n=0
while 1:R=range(n);X=range(1<<n);print(len({min(sum((r[i]>>j&1)<<p[i]*n+p[j]for i in R for j in R)for p in permutations(R))for r in product(*[{k|1<<i for k in X}for i in R])if 0<sum(all((a&s)%a<1>r[j]*(a>>j&1)&~a for a in r for j in R)for s in X)<3}));n+=1
