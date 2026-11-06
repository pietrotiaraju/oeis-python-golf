Q=[[t:=1]]*4
while Q:=[[t]+[t:=t+i*x for i,x in enumerate(L)]for L in Q]:print(t);t=0
