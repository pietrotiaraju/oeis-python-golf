from functools import*
from itertools import*
n=3
while 1:
 n+=1;Q=list(permutations(range(n)))
 f=cache(lambda r,C:r>3or sum(f(r+1,tuple(C[j]|1<<p[j]for j in range(n)))for p in Q if p[0]==r and all(~C[j]>>p[j]&1 for j in range(n))))
 print(f(1,tuple(1<<j for j in range(n))))
