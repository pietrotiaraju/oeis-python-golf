from itertools import*
def g(T):
 N=n*n;U=T+[N]*-~N*n;R=range(n)
 return all(len({U[U[a*n+b]*n+c],U[a*n+U[b*n+c]],N})<3for a,b,c in product(R,R,R))and all(next((w>t for j,t in enumerate(T)if(w:=(*i,N).index(U[i[j//n]*s+i[j%n]*n//s]))-t),1)for i in permutations(R)for s in(1,n))and(sum(g(T+[v])for v in R)if len(T)<N else all(a in{U[U[a*n+x]*n+a]for x in R}for a in R))
n=1
while[print(g([]))]:n+=1
