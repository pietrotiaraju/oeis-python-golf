from math import comb as C
n=1
while 1:print(3*sum(C(n,2)*C(n,k+2)*C(n,k)*C(n-2,k)+n*n*C(n,k+1)*C(n-1,k+1)*C(n-1,k)for k in range(n-1)));n+=1
