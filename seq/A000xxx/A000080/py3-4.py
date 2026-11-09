from itertools import*
e=lambda T,s={0}:{*R}in[s:=s|{*t}for t in T*n if s&{*t}]
n=3;C=combinations
while R:=range(n):print(len({min(sum(1<<sum(1<<p[i]for i in t)for t in T)for p in permutations(R))for k in R for T in C(C(R,3),k+1)if e(T)>any(map(e,C(T,k)))}));n+=1
