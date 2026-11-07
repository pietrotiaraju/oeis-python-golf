from itertools import*
n=0
while[R:=range(n),print(sum(all(a|r[j]*(a>>j&1)==a for a in r for j in R)for r in product(*[{k|1<<i for k in range(1<<n)}for i in R])))]:n+=1
