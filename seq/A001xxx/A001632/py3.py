m=0
while m:=m+2:
 P=k=p=1
 while(g:=p*P%k)-m:p+=g;P*=k;k+=1
 print(p+m)
