from itertools import*
F=frozenset
E=lambda a,b:1<<((c:=max(a,b))*~-c//2+a+b-c)
M=lambda V:(e|E(a,b)for a,*W in[V]for b in W for e in M([x for x in W if x!=b]))if V else[0]
H=lambda E:((x,*t)for x in L if x&E&-E and x&E==x for t in H(E^x))if E else[()]
n=2
while 1:
 R=range(n);L=[*M(R)];S=set();c=0
 for t in H((1<<n*~-n//2)-1):
  if F(t)in S:continue
  c+=1
  for p in permutations(R):
   B=[E(p[i],p[j])for j in R for i in range(j)]
   S.add(F(sum(b*(x>>k&1)for k,b in enumerate(B))for x in t))
 print(c);n+=2
