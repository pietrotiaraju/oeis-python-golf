n=1
while 1:
 a=0;f=1
 for k in range(n-1,0,-1):f*=k;a=a*n+f
 print(a);n+=1
