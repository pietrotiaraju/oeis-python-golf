from math import*
f=lambda m,r,*P:~-m*f(m-1,r+1,*P)+f(m-1,1,r,*P)if m else sum(prod(sum(d*(r*-~(x:=e&r)%d<1)for d in P+P)**(2-x)for r in P)for e in(0,1))
R=[1];E=[n:=0];F=2
while 1:n+=1;F*=n;R=[f(n,1)//F]+R;E+=n*R[0]-sum(E[d]*sum(R[d::d])for d in range(1,n)),;print(E[n]//n)
