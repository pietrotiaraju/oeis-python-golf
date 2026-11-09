f=lambda p,S:B<=len(S)or sum(f(w,S|{w})for d in(1,B,~B)for w in{p+d,p-d}-S)
B=1
while[print(+f(0,{0}))]:B+=1
