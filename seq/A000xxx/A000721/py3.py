from itertools import*
n=1
while 1:
 t=c=0;X=2**2**n
 for*m,p in product(range(2**n),permutations(range(n))):
  for w in p:m+=[y^1<<w for y in m];P=1
  for x in m:
   Q=1
   while~m[x]:m[x],x=-1,m[x];Q*=X;P+=(m[x]<0)*P*Q
  t+=P//X**2**~-n%X;c+=1
 print(t//c);n+=1
