from itertools import*
n=o=0
while 1:R=range(2**n);print(-o+(o:=len({min(sum((f>>(s^sum((x>>i&1)<<p[i]for i in p))&1)<<x for x in R)for p in permutations(R[:n])for s in R)for f in range(2**2**n)})));n+=1
