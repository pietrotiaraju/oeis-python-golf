P=2,3,5,7,11,13;n=1
f=lambda S:n<=len(S)or sum(f(S|{c})for c in{s*p for s in S for p in P}if c>max(S)and{c//p for p in P if c%p<1}<=S)
while[print(+f({1}))]:n+=1
