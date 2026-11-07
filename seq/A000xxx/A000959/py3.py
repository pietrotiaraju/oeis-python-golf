L=[];m=0
while 1:
 m+=1;q=m
 if all(q%k*(q:=q-q//k)for k in L):print(m);L+=[m+1//m]
