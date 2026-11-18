def f(n,U,S):
 t=0
 while U:c=U.pop();N={c+1,c-1,c+K,c-K,c+K*K,c-K*K};t+=n<2or f(n-1,U+[d for d in N-S if d>0],S|N)
 return t
K=3
while 1:print(f(K-2,[0],{0}));K+=1
