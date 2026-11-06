r=[s:=1]
while[print(s)]:
 for s in 0,r[0]:r=[s:=s-2*x for x in[s]+r[::-1]]
