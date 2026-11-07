f=lambda p,S:sum(f(w,S|{w})for d in(1,B,B*B)for w in{p+d,p-d}-S)if len(S)<B else p%B<1
B=1
while[print(+f(0,{0}))]:B+=1
