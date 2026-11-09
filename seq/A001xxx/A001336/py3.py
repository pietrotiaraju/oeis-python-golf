f=lambda p,S:B<=len(S)or sum(f(w,S|{w})for i in range(16)if{w:=p+B**(i%4)-B**(i//4)}-S)
B=1
while[print(+f(0,{0}))]:B+=1
