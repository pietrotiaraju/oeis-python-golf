r=[s:=2];p=1
while[print(s)]:
 for s in 0,(p:=p*-4)*p^p:r=[s:=s+5*x for x in[0]+r[::-1]]