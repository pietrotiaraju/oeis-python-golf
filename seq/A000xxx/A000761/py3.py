f=lambda p,S:sum(f(w,S|{w})for d in(1,B,B*B)for w in{p+d,p-d}-S)if len(S)<B-2 else p%B<1
B=5
while[print(f(2,{2}))]:B+=1
