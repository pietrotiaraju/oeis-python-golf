from math import*
n=2
while[print(1+sum(comb(m,b)*comb(n+b+~m,m-1)*sum((-1)**j*comb(b,j)*(b-j)**(m-2)for j in range(m))for m in range(2,n-1)for b in range(m)))]:n+=1
