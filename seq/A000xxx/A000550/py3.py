L=[[]for _ in range(4)];n=0
while 1:
 n+=1
 for h in range(4):L[h]+=[1 if n==1 else sum(sum(L[h][n-d*j-1]for j in range(1,(n-1)//d+1))*d*L[h-1][d-1]for d in range(1,n))//(n-1)if h else 0]
 if n>=8:
  R=[a-b for a,b in zip(L[3],L[2])]
  print((sum(R[j-1]*R[n-j-1]for j in range(1,n))+(R[n//2-1]if n%2==0 else 0))//2)
