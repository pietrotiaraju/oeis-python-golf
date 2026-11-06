R=[1,n:=1]
while[print(R[n])]:n+=1;R+=sum(d*d*~-d*(d-2)*sum(R[d::d])for d in range(-n,0))//6//n,
