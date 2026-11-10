def f(n,U,S,P):
 while U:c=U.pop();N={c+1,c-1,c+K,c-K};Q=P+[c];yield from n>1and f(n-1,U+[*N-S],S|N,Q)or[Q]
m=1
while[K:=3*m,print(sum(3*m-sum(c+d in Q for c in Q for d in(1,K))>=len({c+d for c in Q for d in(0,1,K,K+1)})and sorted(Q)==min(sorted(c-min(C)for c in C)for r in(0,1)for s in(K,-K)for t in(1,-1)for C in[[s*Y[r]+t*Y[r-1]for c in Q for Y in[divmod(c+m,K)]]])for Q in f(m,[0],{*range(-2*K,1)},[])))]:m+=1
