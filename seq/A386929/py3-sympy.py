from sympy import*
n=1
while[print(next((b for b in range(2,11)if isprime(sum(n//b**i%b*10**i for i in range(n)))),0))]:n+=1
