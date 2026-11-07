from decimal import*
c=getcontext();n=p=1
while 1:
 p+=1;c.prec=2*p;L=c.ln(2)*~-n;t=s=2*L.sqrt()
 for k in range(1,4*p):t*=L/k;s+=t/(2*k+1)
 w=s/10**p;n+=round(s-w)==round(s+w)!=print(round(s)or 1)
