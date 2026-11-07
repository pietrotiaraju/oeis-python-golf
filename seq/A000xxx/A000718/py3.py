t=c=1;r=[1]
while[print(t)]:r=[t:=t+x for x in[c-t]+r[::-1]];c+=len(r)