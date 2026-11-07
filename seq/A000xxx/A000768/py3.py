f=lambda p,S:sum(f(w,S|{w})for a in U for b in U if{w:=p+a-b}-S)if len(S)<B-3 else p%B<1
B=7
while 1:U=0,-1,~B,B*B;print(f(3,{3}));B+=1
