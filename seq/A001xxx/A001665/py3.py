f=lambda p,S:n<len(S)or sum(f(w,S|{w})for d in(1,B,B-1)for w in{p+d,p-d}-S if~w&B+1)
n=B=0
while[print(+f(n,{n}))]:n+=1;B=2<<n
