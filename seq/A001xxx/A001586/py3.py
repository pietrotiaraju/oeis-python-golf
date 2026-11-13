r=[1];k=s=-1
while[print(r[k])]:r=[s:=s+x for x in[-s]+r[:k-1:-1]+r[k::-1]];k-=1
