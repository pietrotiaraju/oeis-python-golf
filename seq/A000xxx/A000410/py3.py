from functools import*
from itertools import*
f=cache(lambda M:M==()or sum((-1)**i*f(M[:i]+M[i+1:])for i,r in enumerate(M)if 2*r>>len(M)&1))
n=1
while[print(sum(0==f(V)for V in combinations(range(1,1<<n),n)))]:n+=1
