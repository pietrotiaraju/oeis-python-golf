import math
f=lambda r,*L:r<1and(c:=lambda d:sum(2**sum(map(math.gcd,L,[d*t]*n))for t in range(P))//P-1)and 8**c(1)+(21<<c(1)+c(2))+(56<<c(3))+(42<<(c(2)+c(4))//2)+(48<<(c(7)-c(1))//2)or sum(f(r+~k,*L,~k)for k in range(r))//r
n=P=1
while[print(f(n)//168)]:n+=1;P*=n
