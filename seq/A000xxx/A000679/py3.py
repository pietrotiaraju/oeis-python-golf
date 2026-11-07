from itertools import*
c=lambda G,d=0:min([(*r,)for T in product(*[G[0]]*d)if[L:=[0]]if(r:=[L.index(y)for x in L for g in T if(y:=G[x][g])in L or[L.append(y)]])if L[len(G)-1:]]or[c(G,d+1)])
Q={0:[[0]]}
while[print(len(Q))]:Q={c(G:=[[2*t[t[x][(R,A)[e][k]]][h*e*j]+e^j for k in R for j in(0,1)]for x in R for e in(0,1)]):G for t in Q.values()for R in[t[0]]for A in permutations(R)for h in R if all(A[t[a][b]]==t[A[a]][A[b]]and t[A[A[b]]][A[h]]==t[h][b]for a in R for b in R)}
