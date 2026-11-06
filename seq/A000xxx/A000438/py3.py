from functools import*
def M(V):
 if not V:yield 0
 else:
  a,*W=V
  for b in W:
   for e in M([x for x in W if x!=b]):yield e|1<<(b*(b-1)//2+a)
n=2
while 1:
 L=list(M(range(n)))
 @cache
 def F(E):
  if not E:return 1
  p=E&-E
  return sum(F(E^x)for x in L if x&p and x&E==x)
 print(F((1<<(n*(n-1)//2))-1));n+=2
