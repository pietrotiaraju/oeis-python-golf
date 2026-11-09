f=lambda p,S:p%-~B<1if B<len(S)*2else sum(f(w,S|{w})for w in{~p,1-p,B-p,B*B-p}-S)
B=5
while[print(f(2,{2}))]:B+=4
