from functools import*
def M(V):
 if V:
  a,*W=V
  for b in W:
   for e in M([x for x in W if x!=b]):yield e|1<<(b*(b-1)//2+a)
 else:yield 0
n=2
while 1:
 L=list(M(range(n)))
 F=cache(lambda E:E<1or sum(F(E^x)for x in L if x&E&-E and x&E==x))
 print(F((1<<(n*(n-1)//2))-1));n+=2
