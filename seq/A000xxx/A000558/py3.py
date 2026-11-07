L=[0]
while 1:L=[s:=~-2**len(L)]+[s:=s+len(L)*L.pop(0)for _ in L*1];print(s)
