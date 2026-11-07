g=lambda B,s,x=[]:(x and g(x+[-1],s)or s==0)+sum(g(B[1:],s+1-(3*v+2<<(x>[])),x+[v])for v in range(min(B[1]+1,s,*x[-1:])))
*a,n=1,0
while 1:n+=1;a+=sum(d*(d%2or-d//4)*sum(a[d::d])for d in range(-n,0))//-n,;print(a[-1]-g([n]*3*n,n))
