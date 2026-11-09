def f(n,U,S,t=0):
 while U:c=U.pop();N={c+1,c-1,c+K,c-K,c-~K,c+~K};t+=n<2or f(n-1,U+[*N-S],S|N)
 return t
K=1
while[print(f(K,[0],{*range(-2*K,1)}))]:K+=1
