from math import comb as C
n=1
while[print(3*sum(C(j,2)*C(n,j)*(C(n,j)*C(n,j-2)+2*C(n,j-1)**2)for j in range(2,n+1)))]:n+=1
