from math import*
k=0
while k:=k+1:
 D=range(1,2*k);b=min(k//s**2for s in D if k%s**2<1);N=3*k*k-3;S={k<2or b<2and any(N%d+(T:=N//d-d-6*k)%12<1>-T for d in D)}
 for f in[f for f in D if N%f**2<1<b]:
  M=N//f//f;R=[0];m=p=1
  while m<M:
   p+=1
   while M%(q:=m*p)<1:R=[y for x in R for y in range(x,q,m)if(y*y-b)%q<1];m=q
  for P in R:
   Q,g,u,w=M,1,f*M,-f*P
   while{t:=(P,Q,g,u,w)}-S:S|={t,Q+g==0==u-k%2*3};a=(P+isqrt(b)+(Q<0))//Q;P=a*Q-P;Q=(b-P*P)//Q;g=-g;u,w=(a*u+w)%6,u
 if{1}&S:print(k)
