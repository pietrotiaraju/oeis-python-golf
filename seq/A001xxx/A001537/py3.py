from math import*
n=1
while 1:
 N=2**n;D={};S=[(len(C),e)for e in range(1,N,2)for k in range(e)if gcd(k,e)<2>k-min(C:={k*2**j%e for j in range(e)})+1]
 def R(r,s,F,w,c=0,p=0,z=0):
  if s:d,e=s[0];R(r,s[1:],F,w);[R(r-d*x,s,(*(f*(x*b<(y:=t&-t))<<d*min(x,y>>t%e*N)for t,f in enumerate(F)),),w//(2**(d*(C:=c*(x==p)+1))-1)>>d*(2*z+x-C)+(e<2),C,x,z+x)for x in range(p or 1,r//d+1)for b in{0,e<2}]
  elif r<1:D[F]=D.get(F,0)+w
 R(n,S,(1,)*-~N,K:=factorial(N));T=0
 for F,c in D.items():
  F=[*F];z=c*c
  for k in range(1,N+1):z*=k**(u:=F[k]//k)*factorial(u);F[k::k]=[f-F[k]for f in F[k::k]]
  T+=z
 print(T//K**2);n+=1
