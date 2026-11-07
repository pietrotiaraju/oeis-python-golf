import math
f=lambda r,*L:r<1and(v:=lambda d:1<<sum(2**sum(map(math.gcd,L,[d*t]*n))for t in range(P))//P)and v(1)**2+6*v(2)+8*v(3)//v(1)or sum(f(r+~k,*L,~k)for k in range(r))//r
n=P=1
while[print(f(n)//24)]:n+=1;P*=n
