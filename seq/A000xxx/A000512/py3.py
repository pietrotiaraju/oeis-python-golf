from math import*
from functools import*
P=lambda n,m=1:[((j,*p),-z*j*~p.count(j))for j in range(m,n+1)for p,z in P(n-j,j)]if n else[((),1)]
n=H=1
while[print(sum(H//r//s*(f:=cache(lambda R,C,h:R==()or C[-1]>(0,)and(sum(comb(g:=gcd(r:=R[0],s),t)*f(R,C[1:]+((C[0][0]-t*r//g,s),),h-t*s//g)for t in range(h+1))if(s:=C[0][1])else h==0and f(R[1:],(*sorted(C),),3))))(R,(*zip([3]*n,S),(9,0)),3)for R,r in P(n)for S,s in P(n))//H)]:n+=1;H*=n*n
