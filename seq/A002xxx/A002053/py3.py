l=[0,1];u=m=1;D={}
while m:=m+1:
 p=D.pop(m,m);x=m+p
 while x in D:x+=p
 D[x]=p;l+=-l[m//p],;u+=l[-1];u+=u<1!=print(m)