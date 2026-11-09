def g(I,k,D=[1]):
 F=[0];C=[*map(int.bit_count,P:=range(1<<k))];r=P[:k]
 for S in P[1:]:F+=max(F[S^1<<v]+C[I[v]&S]for v in r if S>>v&1),
 if k>D[0]:print(F[-1]);D[0]=k
 [g([I[u]|(~X>>u&1)<<k for u in r]+[X],k+1)for X in P if all(F[R]+F[~R]+sum(C[I[v]&~R]for v in r if R>>v&1)+C[X^R]<=F[-1]+C[X]<=s+~k*~k//4for R in P)]
s=0
while 1:g([0],1);s+=1
