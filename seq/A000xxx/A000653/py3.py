from itertools import*
n=1
while 1:
 D={};a=c=0
 for p in permutations(range(n)):
  m=[0];l=[];z=1;c+=1
  for w in p:m+=[y+2**w for y in m]
  for x in m:
   j=0
   while~x:m[x],x=-1,m[x];j+=1
   if j:l+=j,;z*=~-j*l.count(j)
  k=(*sorted(l),);D[k]=d=D.get(k,0)+z;a+=d+d-z
 print(a//c//c);n+=1
