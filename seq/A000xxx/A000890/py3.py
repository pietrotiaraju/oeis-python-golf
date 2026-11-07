from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(42<<(a:=(d:=lambda j,m=2*lcm(*L):sum(R:=[prod((t*j//(g:=gcd(t*j,l))%2*l<1)<<g for l in L)for t in range(m)])//m+(0in R))(1))+d(2))+8**a+224*2**d(3)+384*2**(d(7)-a>>1)+(168<<(d(2)-~d(4)>>1))
n=1
while[print(f(n)//1344)]:n+=1
