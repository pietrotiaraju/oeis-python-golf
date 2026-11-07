r=[t:=0];f=1
while[print(t)]:r=[t:=t+(f:=x)for x in[r[0]+f-t]+r[::-1]]