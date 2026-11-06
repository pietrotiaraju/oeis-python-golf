from itertools import*
n=1
while 1:
 Q=[*permutations(range(n))];C=set()
 def f(L):
  r=len(L)
  if r==n:C.add(min(tuple(sorted(tuple(z.index(b[i])for i in q)for b in T))for T in(L,[*zip(*L)])for q in Q for a in T if(z:=[a[i]for i in q])))
  else:
   for p in Q:
    if p[0]==r and all(x not in c for x,c in zip(p,zip(*L))):f(L+[p])
 f([range(n)]);print(len(C));n+=1
