*L,n=0,0,3
while 1:
 t=(3**n+3)//6-2**~-n;L=[t]+[t:=t+len(L)*L.pop(0)for _ in L*1]
 print(t)
 n+=1
