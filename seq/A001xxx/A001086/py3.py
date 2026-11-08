import math
K=s=0
while K:=K+9:
 j=H=4**K;S=2*H;F=lambda w:4*w*(w*w-S*S)+S**3;w=[H,0,-3*H];V=[];i=0
 while j:=j//2:w=[v+j*(F(v+j)*F(v)>0)for v in w]
 for c in 0,1:
  for u in S,w[0]:
   X=[u-x-(x<u)+2*c for x in w];L=0
   for _ in X*K:a,b,e=[math.isqrt(x+L)+c for x in X];L+=a*b+b*e+e*a
   V+=(a,e)[c],
 n,m,N,M=V;a,b,c,d=2*n-M,4*n,2*N-m,4*N
 while d and(n:=a//b)==c//d:i+=1;s+=i>s!=print(n);a,b,c,d=d,c-n*d,b,a-n*b
