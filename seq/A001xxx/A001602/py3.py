P=k=1
while 1:
 P*=k*k;k+=1;a=b=m=P%k
 while a:a,b=b,(a+b)%k;m+=1
 m and print(m)
