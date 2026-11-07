q=1
while 1:
 q+=1;p=h=2
 while q%p:p+=1
 if p**q%q<1:
  Q=q**3;R=range(N:=q*q+q+1);A=lambda a,b,c=1:a+b and(a+c*b)%p+p*A(a//p,b//p,c)
  while len({*(G:=[t:=1]+[t:=A(t*p%Q,h,t*p//Q)for _ in[0]*Q*Q])})<Q-1:h+=1
  L=[sum(1<<(i+j)%N for i in R if A(A(G[i],G[i*q]),G[i*q*q])<1)for j in R]
  print(max(S.bit_count()*all((S&l).bit_count()<4for l in L)for S in range(1<<N)))
