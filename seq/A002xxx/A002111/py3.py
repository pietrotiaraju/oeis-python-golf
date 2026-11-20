r=[s:=1]
while 1:
 for s in 0,-r[0]:r=[s:=s+x*3for x in[0]+r[::-1]]
 k=len(r);print(3*k*s//(4**k+2**k))
