m=b=c=d=1;a=0
while[print(a)]:m+=1;a,b,c,d=b,c,d,m*(b+c+d)+(m*c+d-b)//2+a+(-1)**m
