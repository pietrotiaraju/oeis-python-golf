n=4
f=lambda k,t,i=2:k<1or t>=V[i]and f(k-1,t-V[i],i)+f(k,t,i+1)
while V:=[M:=n**200]:
 for x in range(n*n):
  r=x*M;N=r*r*M
  while r**3>N:r=(2*r+N//r//r)//3
  V+=r,
 print(f(4,n*M));n+=1
