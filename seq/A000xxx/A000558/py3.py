L=[];n=1
while 1:
 t=2**~-n-1;L=[t]+[t:=t+len(L)*L.pop(0)for _ in L*1]
 if n>=2:print(t)
 n+=1
