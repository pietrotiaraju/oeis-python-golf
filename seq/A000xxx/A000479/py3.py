from itertools import*
f=lambda Q,k:k<1or sum(f([q for q in Q if all(map(int.__ne__,p,q))>(q<p)],k-1)for p in Q)
n=0
while[print(+f([*permutations(range(n))],n))]:n+=1
