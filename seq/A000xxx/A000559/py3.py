L=[c:=0,e:=0]
while 1:L=[s:=(c:=3*c+(e:=e-~e))]+[s:=s+len(L)*L.pop(0)for _ in L*1];print(s)
