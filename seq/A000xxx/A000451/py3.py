P=[];c=[0];n=k=t=0
while 1:
 if n==k*k:
  P+=[n+j*j for j in range(k+1)];c+=[0]*9*k;k+=1
  for p in P:c[n+p]+=1
 while t<c[n]:print(n);t+=1
 n+=1
