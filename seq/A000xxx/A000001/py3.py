from itertools import*
print(0);n=k=1;Q=product
while P:=[*permutations(R:=range(n))]:print(sum(all(t[p[t[a][b]]][p[c]]==p[t[a][t[b][c]]]for a,b,c in Q(R,R,R))for t in Q([R],*batched(P[k:],k))for p in P[:k])//k);k*=n;n+=1
