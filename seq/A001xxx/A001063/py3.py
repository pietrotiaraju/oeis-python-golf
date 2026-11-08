R=[s:=1];d=0
while[print(R[0])]:R=[s:=s+d*x for x in[0]+R];d+=1
