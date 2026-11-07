f=lambda p,S:sum(f(w,S|{w})for a in U for b in U if{w:=p+a-b}-S)if len(S)<B else p%B<1
B=1
while[print(+f(0,{0}))]:B+=1;U=0,-1,~B,B*B
