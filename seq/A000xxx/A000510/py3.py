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
q=1
while 1:
 q+=1;L=P(q)
 if L:
  N=len(L);U=(1<<N)-1;B=0;H=[[l for l in L if l>>j&1]for j in range(N)]
  def f(S,V):
   global B
   n=S.bit_count();B=max(B,n)
   while n+V.bit_count()>B:
    b=V&-V;V-=b;T=S|b;D=0
    for l in H[b.bit_length()-1]:
     if(T&l).bit_count()==3:D|=l
    f(T,V&~D)
  f(0,U);print(B)
