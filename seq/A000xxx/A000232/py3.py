P=k=d=1;L=[]
while 1:
 P*=k*k;k+=1
 if P%k:L=[s:=-k]+[s:=abs(s-x)for x in L];d-=1
 while L[d]>2:print(~d);d+=1
