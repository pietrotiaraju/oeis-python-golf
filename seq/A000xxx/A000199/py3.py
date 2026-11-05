m=1
while r:=[1]*m:
 k=m
 while k:
  for j in range(k,m):r[j]-=r[j-k]
  k-=1;r=[-r[0]]+r
 print(r[m]);m+=2
