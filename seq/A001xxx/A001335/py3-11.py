f=lambda p,S:sum(f(w,S|{w})for d in(1,B,~B)for w in{p+d,p-d}-S)if len(S)<B else 0==p!=B-3
B=1
while[print(+f(0,{.5}))]:B+=1
