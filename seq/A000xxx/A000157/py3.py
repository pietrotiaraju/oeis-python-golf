from itertools import*
n=1
while 1:
 t=k=0
 for*m,p in product(range(2**n),permutations(range(n))):
  for w in p:m+=[y^1<<w for y in m];r=b=1
  for x in m:
   while~m[x]:b&=m[x]!=x;m[x],x=-1,m[x];r<<=m[x]<0
  t+=r<<b;k+=4
 print(t//k);n+=1
