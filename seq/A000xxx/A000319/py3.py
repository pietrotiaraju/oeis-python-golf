P=5;m=0
def G(u):
 a=(P//5+(u>>P)**2)*V;b=2*a
 for c in range(b-3*V,0,-2*V):a,b=c+u*u//-a//(a*b>0),c-u*u//b
 return u*V//a//(a*b>0),u*V//b
while 1:
 P*=2;l=h=V=1<<P;k=0
 try:
  while 0<=l^h<V:m+=k==m!=print(l>>P);l,*_,h=sorted(G(l)+G(h+1));k+=1
 except:0
