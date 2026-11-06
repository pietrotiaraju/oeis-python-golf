from itertools import*
n=1
while 1:
 Q=list(permutations(range(n)));C=set()
 def f(L):
  r=len(L)
  if r==n:
   H=[]
   for T in(L,list(zip(*L))):
    for q in Q:
     for a in T:
      z=[a[q[i]]for i in range(n)]
      H+=[tuple(sorted(tuple(z.index(b[q[i]])for i in range(n))for b in T))]
   C.add(min(H))
  else:
   for p in Q:
    if p[0]==r and all(p[j]not in[b[j]for b in L]for j in range(n)):f(L+[p])
 f([tuple(range(n))]);print(len(C));n+=1
