h=lambda x:sum(sum(d for d in range(4,x-s*s+1,4)if x%d==s*s%d)+x*(s*s==x)-(s>1>x%s**2and h(x//s//s))for s in range(-x,x))
x=4
while[print((h(x)+10)//20)]:x+=4
