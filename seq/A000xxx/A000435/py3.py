n=1
while 1:
 a=0;f=1
 for j in range(1,n):f*=n-j;a=a*n+f
 print(a);n+=1