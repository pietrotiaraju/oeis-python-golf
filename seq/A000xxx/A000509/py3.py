def P(q):
 p=next(p for p in range(2,q+1)if q%p<1);e=0;r=q
 while r%p<1:e+=1;r//=p
 if r>1:return
 R=range(q)
 A=lambda a,b,c=-1:sum((a//p**i-c*(b//p**i))%p*p**i for i in range(e))
 for h in R:
  G=[];t=1
  for _ in R[1:]:
   G+=[t];t=A(t*p,h,t*p//q)
  if t==1 and len(set(G))==q-1:break
 M=lambda a,b:a*b and G[(G.index(a)+G.index(b))%(q-1)]
 return[sum(1<<(x*q+A(M(a,x),b))for x in R)|1<<(q*q+a)for a in R for b in R]+[((1<<q)-1)<<(b*q)|1<<(q*q+q)for b in R]+[((1<<q+1)-1)<<q*q]
q=6
while 1:
 q+=1;L=P(q)
 if L:
  N=len(L);U=(1<<N)-1;B=set();A=(0,1,q,q+1)
  H=[[next(l for l in L if l>>i&l>>j&1)if i!=j else 0 for j in range(N)]for i in range(N)]
  C=0
  for i in A:
   for j in A:C|=H[i][j]
  def f(S,C,V):
   if C==U:B.add(len(S))
   while V:
    b=V&-V;V-=b;j=b.bit_length()-1;D=C
    for i in S:D|=H[i][j]
    f(S+(j,),D,V&~D)
  f(A,C,U&~C);print(sorted(B)[-2])
