import math,functools
f=functools.cache(lambda n,k:k and sum(math.comb(n-1,j)*f(j,k+1)*f(n-j,k-1)for j in range(n))or n<2)
n=0
while 1:n+=1;print(f(n,1))
