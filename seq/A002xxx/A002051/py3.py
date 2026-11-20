r=[t:=1];p=1
while[print(t-p>>1)]:p*=2;r=[t:=t+x for x in[sum(r)-t]+r]
