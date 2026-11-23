from math import*
n=0
while 1:
 n+=1;T=n+3;a=0;R=range(n+1)
 for B in range(T**3):
  l=B%T;m=B//T%T;k=B//T//T;S=l*m*k;u=T-l-m-k
  if~u<0:
   E=[1+2**d<<i for d,q in((1,l),(l,l*m),(l*m,S))for i in range(S)if i%q<q-d];Z=[0]*-~n;W=Z[:];C=[]
   for s in range(2**S):
    v={s:1};q=(2*s.bit_count()-S)**2
    for j in R:
     g=v.get(s,0);Z[j]+=g;W[j]+=q*g;w={}
     for t in(j<n)*[*v]:
      for e in E:w[x]=w.get(x:=t^e*(0<t&e<e),0)+2*v[t]
     v=w
   for i in R:C+=W[i]-sum(comb(i,j)*C[j]*Z[i-j]for j in range(i))>>S,
   a+=(-1)**u*comb(5,u)*C[n]
 print(a)
