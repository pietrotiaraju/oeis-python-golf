from math import*
R=lambda F,r,*L:r and sum(R(F,r+k,*L,k)for k in range(-r,0))//r or F(*L)
n=2
while[print(R(lambda*L:R(F:=lambda*M:n**sum(gcd(a,b)for a in L for b in M),n)+isqrt(F(*L,1,1)//F(2)),n)//2)]:n+=1
