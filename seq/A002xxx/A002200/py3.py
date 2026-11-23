h={1}
while 1:
 h=h-{x:=min(h)}|{2*x,3*x,5*x};n=x+1;a=1
 while any(pow(a,x//q,n)+x%q==1for q in(2,3,5)):a+=1
 pow(a,x,n)-1or print(n)
