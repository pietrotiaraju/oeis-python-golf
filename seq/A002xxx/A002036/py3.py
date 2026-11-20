from decimal import*
c=getcontext();p=F=1
while p:=p+1:
 while round((y:=p/c.ln(p))-(d:=y/c.prec**9))<round(y+d):c.prec+=9
 F%p and print(round(y));F*=p*p