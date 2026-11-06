from itertools import*
n=0
while 1:
 t=k=0
 for*m,p in product(range(2**n),permutations(range(n))):
  r=b=1
  for w in p:m+=[y^1<<w for y in m]
  for x in m:
   while~x:b&=m[x]!=x;m[x],x=-1,m[x];r<<=x<0
  t+=r<<b;k+=2
 print(t//k);n+=1
