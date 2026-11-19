r=7;P=1;q=2
while 1:
 a=h=0
 if P%q:
  while any(pow(d,r//2,r)>1for d in range(q+1))or 0in(r%d for d in range(2,r//q)):r+=8
  while 3*a*a<r:a+=1;h+=sum((x:=b*b+r>>2)%a<1>a*a-x for b in range(-a|1,a,2))
  print(h)
 P*=q*q;q+=1
