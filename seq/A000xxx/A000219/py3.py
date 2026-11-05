R=[n:=1]
while[print(R[-1])]:R+=sum(d*d*sum(R[d::d])for d in range(-n,0))//n,;n+=1