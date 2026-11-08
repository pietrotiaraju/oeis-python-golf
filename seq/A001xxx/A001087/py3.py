f=lambda a=0,*s:a<1or f(*s)+f(*[b for b in s if 0<b&a<a])
m=1
while[print(+f(*range(1,m)))]:m+=1
