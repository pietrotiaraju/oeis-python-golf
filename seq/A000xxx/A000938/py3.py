from math import*
n=1
while[print(2*sum(k%n*(k//n)*gcd(n-k%n,n-k//n)for k in range(n*n))-(n**4-n*n)//6)]:n+=1
