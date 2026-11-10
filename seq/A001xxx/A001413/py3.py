f=lambda p,S:p==0<B^2if B<len(S)else sum(f(w,S|{w})for d in(1,B,B*B)for w in{p+d,p-d}-S)
B=2
while[print(f(0,{.5}))]:B+=2
