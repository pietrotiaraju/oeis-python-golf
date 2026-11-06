import math
f=lambda b,i:b<W[i]or f(b-W[i],i+1)+f(b,i+1)
n=M=1
while 1:M*=2;a,b=[f(n*M,0)for e in(0,1)if[W:=[math.isqrt(x*M*M-e)+e for x in range(1,4*n*n)]]];n+=a==b!=print(a-1)
