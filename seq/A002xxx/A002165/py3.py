from math import*
n=0
while 1:
 n+=1;T=n+3;a=0;R=range(n+1)
 for B in range(T**3*2):
  c=B%2;B//=2;l=B%T;m=B//T%T;k=B//T//T;u=T-l-m-k
  if~u<0:
   P=[(x,y,z)for x in range(l)for y in range(m)for z in range(k)if x+y+z&1==c];S=len(P);Z=[0]*-~n;C=[]
   E=[1<<i|1<<j for i in range(S)for j in range(i)if all(-2<p-q<2 for p,q in zip(P[i],P[j]))]
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
