f=lambda p,S:B<=len(S)or sum(f(w,S|{w})for w in{p+1,p-1,p+B,p-B}-S)
B=1
while[print(+f(0,{0}))]:B+=1
