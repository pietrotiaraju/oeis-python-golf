from math import*
k=2
while[print(sum(k**((g:=gcd(i,k))*k+k%(2*g)>>1)+k**(k*gcd(g,i//k))for i in range(k*k))//2//k//k)]:k+=1
