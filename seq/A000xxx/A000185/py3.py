from math import*
n=5
while[print(n*sum((-1)**j*perm(j,4)*comb(2*n-2-j,j)*perm(n+~j)for j in range(n))//60)]:n+=1