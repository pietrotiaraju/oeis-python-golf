from math import*
n=0
while 1:
 n+=1;T=n//2+3;a=0;R=range(n+1)
 for B in range(T**3):
  l=B%T;m=B//T%T;k=B//T//T;S=l*m*k;u=T-l-m-k
  if~u<0:
   E=[1+2**d<<i for d,q in((1,l),(l,l*m),(l*m,S))for i in range(S)if i%q<q-d];Z=[0]*-~n;C=[]
   for s in range(2**S):
    v={s:1}
    for j in R:
     Z[j]+=v.get(s,0);w={}
     for t in v:
      for e in E:w[x]=w.get(x:=t^e*(0<t&e<e),0)+2*v[t]
     v=w
   for i in R:C+=Z[i]-sum(comb(i-1,j-1)*C[j]*Z[i-j]for j in range(1,i))>>S,
   a+=(-1)**u*comb(5,u)*C[n]
 print(a)
