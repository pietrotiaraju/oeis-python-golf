z=lambda k:b'033544355436688779886655576678778;;::999;<<A=<?=><'[k]-48
f=lambda n:n>99and f(n//10**(e:=~-len(str(n))//3*3or 2))+z(28+e//3)+3*(e<3<3+n%100)+f(n%10**e)or n>19and z(n//10+18)+(n%10>0)+f(n%10)or z(n)
m=n=0
while n:=n+1:
 if f(n)>m:m=f(n);print(n)
