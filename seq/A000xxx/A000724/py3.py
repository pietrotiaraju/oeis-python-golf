import math
f=math.factorial;n=b=c=d=1;a=0
while[print((f(N:=2**n)+(N-1<<N//2)*f(N//2)*b)//f(n)>>2*n)]:a,b,c,d=b,2*b+d+2*n*a,d,d+2*n*c;n+=1
