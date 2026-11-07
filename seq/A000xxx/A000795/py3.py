r=[s:=1]
while[print(s)]:
 for s in 0,1:r=[s:=s+x for x in[0]+r[::-1]]
