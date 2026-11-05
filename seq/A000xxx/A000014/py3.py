A=[0,1];F=A*1;n=0
while[print(F[n]+(A[n//2]*(-1)**n-sum(A[i]*F[n-i]for i in range(n)))//2)]:n+=1;F+=sum(d*A[d]*sum(F[-d::-d])for d in range(1,n+1))//n,;A+=F[-1]-A[-1],
