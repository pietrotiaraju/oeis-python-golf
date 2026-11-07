n=0
while[d:=(n:=n+1)<<(n%4<3)*2]:all(n%k**2for k in range(2,n))and print(sum(0==r<c+(b<1)-a for a in range(d)for b in range(-a,a)for c,r in[divmod(b*b+d,4*a)]))
