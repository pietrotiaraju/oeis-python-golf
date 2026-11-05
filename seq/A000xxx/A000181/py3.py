from math import*
n=4
while[print(n*sum((-1)**j*comb(j,3)*comb(2*n-2-j,j)*perm(n+~j)for j in range(n))//-2)]:n+=1
