from math import*
n=1;P=9
while F:=1<<P:R=range(4*P);L=lambda s,a,u=0:sum(comb(P,k+1)*(u:=u+(-1)**k*F//(a*k+1)**s)for k in R);Q=lambda s:F*(s>P)or isqrt(L(s,1)*(F+F//(2**s-2))//L(s,2)*Q(2*s));S=lambda r,X,v=F:X*sum(v//(k-~k)+r+0*(v:=v*X//-~k//F+r)for k in R)**2;a,b=[(isqrt(32*(Q(2)+t)*S(t>0,n*((L(1,1)>>P)+t))>>4*P)+3)//6for t in(P*P,-P*P)];a-b or print(a);n+=a==b;P+=1
