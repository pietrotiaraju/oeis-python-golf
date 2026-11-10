def f(r,k,p,*L):
 if r:return sum(f(j,k,p+[*range(n-r+1,n-j),n-r],*L,r-j)for j in range(r))//r
 c=1
 for q in range(n*n):
  o=[e:=q]
  while(e:=p[e//n]*k+p[e%n]*n//k)!=q:o+=[e]
  c*=sum(l>>len(o)%l*l for l in L)**(q==min(o))
 return c
n=0
while[print(f(n,1,[])+f(n,n,[])>>1)]:n+=1
