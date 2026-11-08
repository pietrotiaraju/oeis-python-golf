c=b'033544355436688779886655576678778;;::999;<<A=<?=><'
f=lambda n:n>99and f(n//10**(e:=~-len(str(n))//3*3or 2))+c[28+e//3]%48+f(r:=n%10**e)+3*(0<r<100)or n>19and c[n//10+18]%48+f(n%10)or c[n]%48
L=3
while 1:
 n=1
 while f(n)-L:n+=1
 print(n);print(L);L+=1
