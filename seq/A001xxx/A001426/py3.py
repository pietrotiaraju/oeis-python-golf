from itertools import*
def g(T):
 N=n*n;U=T+[N]*-~N*n;R=range(n)
 return all(len({U[U[a*n+b]*n+c],U[a*n+U[b*n+c]],N})<3>len({U[a*n+b],U[b*n+a],N})for a,b,c in product(R,R,R))and all(next((w>t for j,t in enumerate(T)if(w:=(*i,N).index(U[i[j//n]*n+i[j%n]]))-t),1)for i in permutations(R))and(len(T)==N or sum(g(T+[v])for v in R))
n=0
while[print(+g([]))]:n+=1
