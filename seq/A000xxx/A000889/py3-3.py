from itertools import*
n=1
while 1:R=range(2**n);print(len({min(tuple(map((g:=[f[s^sum((x>>i&1)<<p[i]for i in p)]for x in R]).index,g))for p in permutations(R[:n])for s in R)for f in product((0,),*[range(4)]*~-2**n)}));n+=1
