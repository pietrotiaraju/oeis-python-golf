L=[[1]]
while 1:k=0;L=[r:=[sum(r[:(k:=k+1)])for r in L]]+L;print(3*sum(r[::-2])-sum(r)-1//k)
