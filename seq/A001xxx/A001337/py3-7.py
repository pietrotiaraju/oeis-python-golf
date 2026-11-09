f=lambda p,S:sum(f(w,S|{w})for i in range(16)if{w:=p+B**(i%4)-B**(i//4)}-S)if len(S)<B else 0==p<B-3
B=2
while[print(f(0,{.5}))]:B+=1
