P=p=1
while 1:
 P*=p*p;p+=1
 if P%p*p%3==1:
  s=p**6;x=Y=4*s//p;k=1
  while x:x=x*k//(k-~k);Y+=x;k+=1
  c=s-Y*Y//2//s+Y**4//24//s**3;C=[s,c];exec('C+=2*c*C[-1]//s-C[-2],;'*p)
  if sum(C[x**3%p]for x in range(p))**2<p*s*s:print(p)
