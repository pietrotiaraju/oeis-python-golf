M=[];a=b=1
while 1:M=[s:=b]+[s:=s+(s+M.pop(0))*len(M)for _ in M*1];a,b=b,a+b;print(s)
