P=[];n=r=1
while[print(r)]:
 r=n=n+1
 for p in P:r+=r//p>>n%p*n
 if r==n:P+=n,;r+=1
