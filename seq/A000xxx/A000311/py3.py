p=0;R=[1]
while[print(p)]:t=p=0;R=[t:=t+len(R)*(p+(p:=R.pop(0)))for x in R*1]+[t]
