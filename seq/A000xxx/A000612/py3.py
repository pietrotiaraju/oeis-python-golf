from math import*
f=lambda r,*L:r<1and 1<<sum(2**sum(map(gcd,L,[t]*n))for t in range(lcm(*L)))//lcm(*L)-1or sum(f(r+k,*L,k)for k in range(-r,0))//r
n=0
while[print(f(n))]:n+=1
