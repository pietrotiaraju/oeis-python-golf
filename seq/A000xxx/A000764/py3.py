m=0;L=[t:=1]
while[print(t)]:L=[t:=t+x for x in[L[m]-t]+L[:m]+[0]+L[m:][::-1]];m+=1
