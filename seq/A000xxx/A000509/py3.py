from math import*
def plane(q):
 p=next((d for d in range(2,isqrt(q)+1)if q%d==0),q);e=0;r=q
 while r%p==0:e+=1;r//=p
 if r>1:return
 def digits(a,m=e):return[a//p**i%p for i in range(m)]
 def rem(a,b):
  a=a*1;d=len(b)-1
  for j in range(len(a)-1,d-1,-1):
   c=a[j]
   for i in range(d+1):a[j-d+i]=(a[j-d+i]-c*b[i])%p
  return a[:d]
 h=next(digits(z)+[1]for z in range(q)if all(any(rem(digits(z)+[1],digits(w,d)+[1]))for d in range(1,e//2+1)for w in range(p**d)))
 A=[[sum((x+y)%p*p**i for i,(x,y)in enumerate(zip(digits(a),digits(b))))for b in range(q)]for a in range(q)]
 M=[]
 for a in range(q):
  row=[]
  for b in range(q):
   c=[0]*(2*e-1)
   for i,x in enumerate(digits(a)):
    for j,y in enumerate(digits(b)):c[i+j]=(c[i+j]+x*y)%p
   row+=[sum(x*p**i for i,x in enumerate(rem(c,h)))]
  M+=[row]
 X=[(1,a,b)for a in range(q)for b in range(q)]+[(0,1,a)for a in range(q)]+[(0,0,1)]
 return[sum(1<<j for j,x in enumerate(X)if A[A[M[l[0]][x[0]]][M[l[1]][x[1]]]][M[l[2]][x[2]]]==0)for l in X]
q=6
while 1:
 q+=1;L=plane(q)
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
