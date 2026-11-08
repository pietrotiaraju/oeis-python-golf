from itertools import*
n=0
while[R:=range(n),print(sum(all(r[j]*(a>>j&1)&~a<1for a in r for j in R)for r in product(*[{k&~2**i for k in range(1<<n)}for i in R])))]:n+=1
