f=lambda p,S:sum(f(w,S|{w})for d in D if{w:=p+d}-S)if len(S)<B else B-2and p in D
B=0
while 1:D=1,-1,B,-B,B+1,~B;print(+f(0,{0}));B+=1
