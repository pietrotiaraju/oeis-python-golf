from itertools import*
n=0
while P:=[*permutations(range(n))]:print(sum({tuple(a[i]for i in b)for a in H for b in H}=={*H}=={tuple(g.index(h[x])for x in g)for h in H}for k in range(len(P))for H in combinations(P,k+1)for g in P)//len(P));n+=1
