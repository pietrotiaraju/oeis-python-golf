from itertools import*
n=1
while 1:
 T=[]
 for*m,p in product(range(2**n),permutations(range(n))):
  for w in p:m+=[y^1<<w for y in m];l=[];z=1
  for x in m:
   j=0
   while~x:m[x],x=-1,m[x];j+=1
   l+=j,;z*=j<1or~-j*l.count(j)
  T+=[[z]+sorted(l)]
 print(sum(k[0]*T.count(k)for k in T[:len(T)>>n])*2**n//len(T)**2);n+=1
