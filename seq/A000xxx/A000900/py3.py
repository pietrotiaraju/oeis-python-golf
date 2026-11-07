a=b=c=d=1;n=0
while[print(b-d>>1)]:
 if n%2:c,d=d,2*d+~-n*c
 a,b=b,b+n*a;n+=1
