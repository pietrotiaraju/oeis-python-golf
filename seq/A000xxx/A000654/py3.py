from itertools import*
n=1
while 1:
 D={};a=c=0
 for*m,p in product(range(2**n),permutations(range(n))):
  for w in p:m+=[y^1<<w for y in m];l=[];z=1
  for x in m:
   j=0
   while~x:m[x],x=-1,m[x];j+=1
   if j:l+=j,;z*=~-j*l.count(j)
  k=(*sorted(l),);D[k]=d=D.get(k,0)+z;a+=d+d-z;c+=1
 print(a//c//c);n+=1
