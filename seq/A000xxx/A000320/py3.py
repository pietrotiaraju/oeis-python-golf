r=[q:=4,s:=4]
while[print(s)]:
 for s in 0,(q:=10-9*q)&-4:r=[s:=s+x*5for x in[0]+r[::-1]]
