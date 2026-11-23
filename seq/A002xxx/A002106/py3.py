from itertools import*
n=0
while n:=n+1:
 P=[*permutations(range(n))];c=lambda s,x:tuple(s.index(x[j])for j in s);R=[(frozenset(P[:1]),[])];S={0}
 for H,G in R:
  N=[s for s in P if all(c(s,x)in H for x in G)];V={*H}
  for g in P:
   if g in V:continue
   V|={tuple(h[i]for i in y)for y in{c(s,g)for s in N}for h in H};F=K={*H};L=G+[g]
   while F and n**(n>4)*len(K)<=len(P):F={tuple(x[i]for i in s)for x in F for s in L}-K;K|=F
   if not F and(K:=frozenset(K))not in S:
    R+=(K,L),;Q=[K]
    for X in Q:Q+=(Z:={frozenset(c(s,x)for x in X)for s in[(*range(1,n),0),*P[1:2]]}-S);S|=Z
 print(sum(len({x[0]for x in K})==n for K,G in R)+2*(n>4))
