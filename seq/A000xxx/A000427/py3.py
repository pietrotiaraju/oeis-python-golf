d=8
S={frozenset()}
while S:
 T=set()
 for s in S:
  for v in {(0,)*d}|{tuple(x+(j==i)for j,x in enumerate(u))for u in s for i in range(d)}:
   if v not in s and all(tuple(x-(j==i)for j,x in enumerate(v))in s for i in range(d)if v[i]):T.add(s|{v})
 S=T;print(len(S))
