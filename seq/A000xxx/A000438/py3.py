from functools import*
M=lambda V:(e|1<<(b*~-b//2+a)for a,*W in[V]for b in W for e in M([x for x in W if x!=b]))if V else[0]
n=2
while 1:
 L=list(M(range(n)))
 F=cache(lambda E:E<1or sum(F(E^x)for x in L if x&E&-E and x&E==x))
 print(F((1<<(n*(n-1)//2))-1));n+=2
