def f(n,U,S,P):
 t=0
 while U:c=U.pop();N={c+1,c-1,c+K,c-K};Q=P+[c];t+=f(n-1,U+[d for d in N-S if d>0],S|N,Q)if n>1else max(map((L:=[d%K for d in Q if d-K not in Q]).count,L))<3
 return t
K=3
while 1:print(f(K-2,[0],{0},[]));K+=1
