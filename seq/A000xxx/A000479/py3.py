from functools import*
from itertools import*
n=0
while 1:
 L=[sum(1<<(i*n+j)for i,j in enumerate(p))for p in permutations(range(n))]
 @cache
 def F(E):
  if not E:return 1
  p=E&-E
  return sum(F(E^x)for x in L if x&p and x&E==x)
 print(F((1<<(n*n))-1));n+=1
