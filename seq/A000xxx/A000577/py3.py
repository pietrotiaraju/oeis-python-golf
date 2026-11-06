def c(S):
 H=[]
 for k in range(6):
  for b in(0,1):
   T=[[(y,x)if b else(x,y)for x,y in t]for t in S];a=min(x for t in T for x,y in t);d=min(y for t in T for x,y in t)
   H+=[tuple(sorted(tuple(sorted((x-a,y-d)for x,y in t))for t in T))]
  S=[tuple((-y,x+y)for x,y in t)for t in S]
 return min(H)
L={(((0,0),(0,1),(1,0)),)}
while 1:
 print(len(L));K=set()
 for S in L:
  for t in S:
   for i in range(3):
    a,b,d=t[i],t[(i+1)%3],t[(i+2)%3];u=tuple(sorted((a,b,(a[0]+b[0]-d[0],a[1]+b[1]-d[1]))))
    if u not in S:K.add(c([*S,u]))
 L=K
