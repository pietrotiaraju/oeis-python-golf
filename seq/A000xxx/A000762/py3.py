f=lambda p,S:sum(f(w,S|{w})for d in(1,B,B*B)for w in{p+d,p-d}-S)if len(S)<B-3 else p%B<1
B=7
while[print(f(3,{3}))]:B+=1
