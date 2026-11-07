r=[6,s:=6];q=5
while[print(s)]:
 for s in 0,(q:=q*-25)-1|2:r=[s:=s+x*6for x in[0]+r[::-1]]
