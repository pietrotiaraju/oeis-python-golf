f=lambda p,S:sum(f(w,S|{w})for a in U for b in U if{w:=p+a-b}-S)if len(S)<B-2 else p%B<1
B=5
while 1:U=0,-1,~B,B*B;print(f(2,{2}));B+=1
