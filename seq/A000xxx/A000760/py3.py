f=lambda p,S:sum(f(w,S|{w})for d in(1,B,B*B)for w in{p+d,p-d}-S)if len(S)<B-1 else p%B<1
B=3
while[print(f(1,{1}))]:B+=1
