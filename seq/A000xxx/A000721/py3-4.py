from itertools import*
n=1
while 1:R=range(2**n);S={0};print(sum({*f}not in S!=S.update(frozenset(s^sum((x>>i&1)<<p[i]for i in p)for x in f)for p in permutations(R[:n])for s in R)for f in combinations(R,2**~-n)));n+=1
