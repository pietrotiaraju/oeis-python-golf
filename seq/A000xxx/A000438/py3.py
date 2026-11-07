f=lambda c,e=0,*E:e<1or sum(f(c|e<<k,*E)for k in range(m)if c&e<<k<1)
m=1
while[print(+f(int(('0'*m+'1')*m,2),*[1<<a*m|1<<b*m for b in range(m)for a in range(b)]))]:m+=2
