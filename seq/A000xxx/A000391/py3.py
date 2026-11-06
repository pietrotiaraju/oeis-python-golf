R=[1,n:=1]
while[print(R[n])]:n+=1;R+=sum(d*d*~-d*(d-2)*(3-d)*sum(R[d::d])for d in range(-n,0))//24//n,
