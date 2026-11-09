N=1
while 1:
 N*=2;s={-1}
 for f in range(a:=2**N):
  a-=f in s;q=[f]
  for g in q:
   if{g}-s:s|={g};q+=g^2**N//3,*(sum((g>>(x**j%2^x%2*N+x>>1)&1)<<x for x in range(N))for j in(0,1))
 print(a)
