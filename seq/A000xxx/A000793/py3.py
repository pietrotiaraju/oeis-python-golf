from math import*
f=lambda n,m=2,l=1:max([l]+[f(n-k,k+1,lcm(l,k))for k in range(m,n+1)])
n=0
while[print(f(n))]:n+=1
