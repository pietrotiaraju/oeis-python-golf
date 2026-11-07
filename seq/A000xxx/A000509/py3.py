def f(S,C,V,k=0):
 if C+1>>N:B.add(k)
 while V:b=V&-V;V-=b;f(S|b,T:=C|b|sum(l^b for l in L if l&b>0<l&S),V&~T,k+1);V*=k>3
q=6
while 1:
 q+=1;p=h=2
 while q%p:p+=1
 if p**q%q<1:
  Q=q**3;R=range(N:=q*q+q+1);A=lambda a,b,c=1:a+b and(a+c*b)%p+p*A(a//p,b//p,c)
  while len({*(G:=[t:=1]+[t:=A(t*p%Q,h,t*p//Q)for _ in[0]*Q*Q])})<Q-1:h+=1
  L=[sum(1<<(i+j)%N for i in R if A(A(G[i],G[i*q]),G[i*q*q])<1)for j in R];B={0};f(0,0,2**N-1);print(sorted(B)[-2])
