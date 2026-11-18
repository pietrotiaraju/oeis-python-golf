from itertools import*
n=0
while 1:R=range(n);X=range(1<<n);print(sum(0<sum(all((a&s)%a<1>r[j]*(a>>j&1)&~a for a in r for j in R)for s in X)<<n-len({*r})<3for r in product(*[{k|1<<i for k in X}for i in R])));n+=1
