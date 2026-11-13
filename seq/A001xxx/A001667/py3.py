f=lambda p,S:sum(f(w,S|{w})if B>len(S)else w==0for d in(1,B,B*B,B*B-~B)for w in{p+d,p-d}-S)
B=4
while[print(8*f(1,{1,.5}))]:B+=2
