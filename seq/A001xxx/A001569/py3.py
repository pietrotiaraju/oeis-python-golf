P=[s:=1]
while[print(s)]:k=d=len(P);P=[s:=-P[0]]+[s:=s+d*(k:=k-1)*p for p in P]
