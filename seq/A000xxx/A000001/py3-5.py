from itertools import*
n=0
while P:=[*permutations(range(n))]:print(sum(all(t[p[c]][p[t[b][a]]]==p[t[t[c][b]][a]]for a,b,c in product(p,p,p))for t in combinations(P,n)for p in P)*n//len(P));n+=1
