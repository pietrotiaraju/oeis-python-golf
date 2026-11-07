t=p=1;r=[1]
while[print(t)]:r=[t:=t+x for x in[p-t]+r[::-1]];p*=2