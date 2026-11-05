from math import*
n=a=m=q=k=0
while R:=range(-(r:=isqrt(n:=n+1)),r+1):
 A=sum(2*isqrt(t)+1for x in R for y in R if(t:=n-x*x-y*y)>=0)
 while abs(d:=abs(A*2**k-isqrt(q*n**3))-abs(a*2**k-isqrt(q*m**3)))<=A:k+=3;q=sum(32*4**k//i//i//comb(2*i,i)for i in range(1,k))
 if d>0:print(m:=n);a=A
