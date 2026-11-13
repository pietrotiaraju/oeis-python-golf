q=[0];r=[2];k=-1
while[print(r[k])]:q,r=r,[s:=-4*q[0]]+[s:=s+3*x for x in r[:k-1:-1]+r[k::-1]];k-=1
