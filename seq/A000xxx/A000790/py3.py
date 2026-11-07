n=0
while 1:
 c=4;P=12
 while(n**c-n+P)%c:P*=c;c+=1
 print(c);n+=1
