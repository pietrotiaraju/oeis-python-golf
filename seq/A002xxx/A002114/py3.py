r=[s:=1]
while 1:
 for s in 0,-r[0]:r=[s:=s+x*3for x in[0]+r[::-1]]
 print(s>>len(r))
