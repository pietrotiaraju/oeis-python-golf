from math import*
n=1
while n:=n+1:all(gcd(n,d**3)-d*d for d in range(2,n))and print(n)