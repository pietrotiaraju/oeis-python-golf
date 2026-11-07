from math import*
f=lambda r,*L:r<1or sum(f(r+k,*L,k)<<k*(k+3)//6+1-sum(sum(k*d*e//lcm(k,d,e)for e in(*L,k))+gcd(k+d,2*k)for d in L)//2for k in range(-r,0))//r
n=0
while[print(+f(n))]:n+=1
