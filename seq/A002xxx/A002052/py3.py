p=3;r=m=1
while 1:
 r+=(r+1)**2<p;S=[1]
 for d in S:m=r-(r+m)%d;S+=[e:=(p-m*m)//d]*(e>1)
 all((x*x-p)%q or q in S for q in range(r+1)for x in range(q))and print(p);p+=4