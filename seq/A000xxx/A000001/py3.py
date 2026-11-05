from itertools import*
print(0);n=1;Q=product
while P:=[*permutations(R:=range(n))]:k=len(P)//n;print(sum(all(p[t[a][b]]==t[p[a]][p[b]]for a,b in Q(R,R))for t in Q(*batched(P,k))if all(t[t[a][b]][c]==t[a][t[b][c]]for a,b,c in Q(R,R,R))for p in P)//k);n+=1
