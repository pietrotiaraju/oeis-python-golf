from math import*
f=lambda r,*L:r and sum(f(r+~k,*L,~k)for k in range(r))//r or 3**(sum(3**sum(map(gcd,L,[t]*n))for t in range(N))//N)
n=N=1
while[print(f(n))]:n+=1;N*=n
