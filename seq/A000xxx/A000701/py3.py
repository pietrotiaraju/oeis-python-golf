L=[[1]]
while[print(sum(L[0][-2::-2]))]:k=0;L=[[sum(r[:(k:=k+1)])for r in L]]+L
