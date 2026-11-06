a,b=0,1
while[print(sum(((~k*a-1)%b-~a)%2<<k for k in range(b)))]:a,b=b,a+b-a%b*2
