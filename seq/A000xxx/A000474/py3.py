from itertools import*
M=lambda V:(e|1<<(b*~-b//2+a)for a,*W in[V]for b in W for e in M([x for x in W if x!=b]))if V else[0]
H=lambda E:((x,*t)for x in L if x&E&-E and x&E==x for t in H(E^x))if E else[()]
n=2
while 1:
 L=list(M(range(n)));A=[(i,j)for j in range(n)for i in range(j)];S=set();c=0
 for t in H((1<<len(A))-1):
  if frozenset(t)in S:continue
  c+=1;Q=[[k for k in range(len(A))if x>>k&1]for x in t]
  for p in permutations(range(n)):
   B=[1<<((b:=max(p[i],p[j]))*(b-1)//2+min(p[i],p[j]))for i,j in A]
   S.add(frozenset(sum(B[k]for k in q)for q in Q))
 print(c);n+=2
