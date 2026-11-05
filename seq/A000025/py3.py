m=0
while 1:
 r=[1]*-~m;k=m
 while k:
  for j in[*range(k,m+1)]*2:r[j]-=r[j-k]
  k-=1;r=[1]+[0]*2*k+r
 print(r[m]);m+=1
