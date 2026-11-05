from sympy import*
n=1;k=0
while[print(sum(mobius(d)*((d%2<<n//d)+(n<<n//d//2+1))for d in divisors(n))//4//n)]:n+=k;k=1
