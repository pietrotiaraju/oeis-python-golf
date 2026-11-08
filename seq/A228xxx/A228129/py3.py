R=[n:=1]
while 1:R+=sum(d//2*d*sum(R[d::d])for d in range(-n,-1))//n,;print(R[-1]or 1);n+=1
