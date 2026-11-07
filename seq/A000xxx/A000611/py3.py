from itertools import*
f=lambda p,C:p[0]>n-2or sum(f(q,D)for D in[[q for q in C if not{*zip(p,q)}&{*zip(q,p)}]]for q in D if q[0]-p[0]<2)
n=1
while[print(+f(r:=range(n),permutations(r)))]:n+=1
