r=[s:=2];p=1
while[print(s)]:
 for s in 0,(p:=p*-25)-1|2:r=[s:=s+6*x for x in[0]+r[::-1]]