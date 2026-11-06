def c(S):
 H=[]
 for k in range(6):
  for b in(0,1):
   T=[(y,x)if b else(x,y)for x,y in S];a=min(x for x,y in T)//3*3;d=min(y for x,y in T)//3*3
   H+=[tuple(sorted((x-a,y-d)for x,y in T))]
  S=[(-y,x+y)for x,y in S]
 return min(H)
L={((1,1),)}
while 1:
 print(len(L));L={c([*S,u])for S in L for x,y in S for a,b in[(1,1),(-2,1),(1,-2)]for d in[3-2*(x%3)]for u in[(x+a*d,y+b*d)]if u not in S}
