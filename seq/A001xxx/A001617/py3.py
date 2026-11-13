from math import*
n=1
while[print(1+sum((gcd(x,c,n//c)<2)*(1-6*(x<gcd(c,n//c)))-c//n*(3*(x*x%n==n-1)+4*(-~x*x%n==n-1))for c in range(1,n+1)if n%c<1for x in range(c))//12)]:n+=1
