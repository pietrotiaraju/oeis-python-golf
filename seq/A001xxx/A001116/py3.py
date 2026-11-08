from fractions import*
from math import*
O=sumprod
S=lambda Q:[[Q[0][0]*b-a*c for b,c in zip(r,Q[0][1:])]for a,*r in Q[1:]]
D=lambda Q:Q==[]or(d:=Q[0][0])>0and D(S(Q))*d//d**~-len(Q)
V=lambda Q,b:Q and[(((z-O(r,y))//d,*y),(z*z+v)//d)for d,*r in[Q[0]]for y,v in V(S(Q),d*b)for w in[isqrt(d*b-v)]for z in range((O(r,y)+w)%d-w,w+1,d)]or[((),0)]
n=0
while 1:
 w=range(n);K=[[[1+(i==j)for j in w]for i in w]][:n>1];b=n
 for P in K:
  L=V(P,P[0][0]);m=min(v for x,v in L if v);G=[*{tuple(a*c for a in x for c in x)for x,v in L if v==m}];b=max(b,len(G));e=range(n*n);L=[[i==j for i in e]for j in e];C=[]
  for g in G:
   for l in L:
    if s:=O(l,g):L,C=[[[(a*s-b*O(m,g))*s for a,b in zip(m,l)]for m in X]for X in(L,C)];C+=[a*s for a in l],;break
   else:W=[(f,O(f,g),{e for e in G[:G.index(g)]if O(f,e)==0})for f in C];C=[f for f,d,z in W if d>=0]+[[s*b-t*a for a,b in zip(p,m)]for p,s,y in W for m,t,z in W if s>0>t and sum(y&z<=x for f,d,x in W)<3]
  for f in C:
   M=R=[[f[i*n+j]+f[j*n+i]for j in w]for i in w];B=m
   while D(M)<1or any(0<v<q*m for x,v in V(M,q*m)):
    if c:=[(v-m,-k)for x,v in V(P,B)if(k:=O(x,map(O,R,[x]*n)))<0]:p,q=min(c,key=lambda t:Fraction(*t));M=[[q*a+p*b for a,b in zip(*z)]for z in zip(P,R)]
    B*=2
   Q=[[a//gcd(*sum(M,[]))for a in r]for r in M];K+=[Q]*all(D(A)-D(Q)or 1-(T:=lambda c=[],k=0:k==n or any(T(c+[x],k+1)for x,v in V(A,Q[k][k])if[O(x,map(O,A,[y]*n))for y in c+[x]]==Q[k][:k+1]))()for A in K)
 print(2*b);n+=1
