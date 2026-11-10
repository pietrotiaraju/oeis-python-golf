N=m=1
while s:=[1]*(N:=2*N):
 L=[];r=1
 for i in range(2,N):s[i*i::i]=[0]*(-i--N//i);L+=[i]*s[i]
 while~(i:=bytes(map(2 .__lt__,L:=[abs(x-y)for x,y in zip(L,L[1:])])).find(1)):r+i>m!=print(m:=r+i);r+=1
