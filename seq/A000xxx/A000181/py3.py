a=1;b=c=0;n=2
while[print((n+2)*abs(3*(b-c)-n*(~b+4*c)-5*a)//6)]:a,b,c=b,c,n*(b-c)-a;n+=1
