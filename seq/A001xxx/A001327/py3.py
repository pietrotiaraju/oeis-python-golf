from math import*
f=lambda r,*L:r and sum(f(r+k,*L,(k,o))for k in range(-r,0)for o in b'')//r//6or(m:=lcm(*map(prod,L)))and 3**(sum(prod((3>>t//(d:=gcd(t,k))%o*~-o)**d for k,o in L)for t in range(m))//m)
n=1
while[print(f(n))]:n+=1
