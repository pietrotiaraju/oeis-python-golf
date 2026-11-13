from decimal import*
getcontext().prec=MAX_PREC
n=0;p=1
while 1:v=2*n*Context(p).ln(n or 1);a,b=round(v-(w:=v.scaleb(1-p))),round(v+w);p+=b-a;n+=a==b!=print(a)
