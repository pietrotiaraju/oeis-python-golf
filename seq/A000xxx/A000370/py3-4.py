from itertools import*
n=0
while 1:R=range(2**n);print(len({min(sum((f>>(s^sum((x>>i&1)<<p[i]for i in p))&1^k)<<x for x in R)for p in permutations(R[:n])for s in R for k in(0,1))for f in range(2**2**n)}));n+=1
