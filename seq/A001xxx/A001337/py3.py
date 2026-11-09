f=lambda p,S:sum(f(w,S|{w})for d in D if{w:=p+d}-S)if len(S)<B else B>2and p in D
B=1
while[print(+f(0,{0}))]:B+=1;D={B**(i%4)-B**(i//4)for i in range(16)}
