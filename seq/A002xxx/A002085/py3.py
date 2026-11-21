r=[1,s:=1]
while[print(s//(s&-s))]:
 for s in 0,1:r=[s:=s+x for x in[0]+r[::-1]]
