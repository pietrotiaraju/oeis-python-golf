f=lambda p,S:p%-~B<1if B<len(S)*2else sum(f(w,S|{w})for w in{~p,1-p,B-p,B*B-p}-S)
B=1
while[print(+f(0,{0}))]:B+=4
