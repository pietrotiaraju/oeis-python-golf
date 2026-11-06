n=2;A=[0,1,0,0,0,0]
while 1:
 n+=1;A=[0]+[k*A[k]+2*A[k-1]+(n-k)*A[k-2]*(k>1)for k in range(1,6)]
 if n>5:print(A[5])
