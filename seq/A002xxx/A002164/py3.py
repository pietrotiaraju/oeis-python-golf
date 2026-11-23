from math import*
C=[0,1,0];N=0
while 1:
 N+=1;R=range(2*N+3);T=[0]*5*N;K,C=C,[]
 for s in range(2**N):
  v={s:1}
  for j in R:
   T[j]+=v.get(s,0);w={}
   for t in v:
    for i in range(N):w[u]=w.get(u:=t^(0<t>>i&3<3)*3<<i,0)+2*v[t]
   v=w
 for n in R:C+=T[n]-sum(comb(n-1,j-1)*C[j]*T[n-j]for j in range(1,n))>>N,
 for n in R[-4:-2]:print(C[n]-K[n])
