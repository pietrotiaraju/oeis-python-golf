from math import*
print(n:=1);P=9
while F:=1<<P:L=lambda s,a,u=0:sum(comb(P,k+1)*(u:=u+(-1)**k*F//(a*k+1)**s)for k in range(P));Q=lambda s:F*(s>P)or isqrt(L(s,1)*(F+F//(2**s-2))//L(s,2)*Q(2*s));a,b=[isqrt((Q(2)+t<<2*n+1)//n//((L(1,1)>>P)-t))+1>>1for t in(P*P,-P*P)];a-b or print(a);n+=a==b;P+=1
