w=lambda n:n>99and w(n//10**(e:=~-len(str(n))//3*3or 2))+1+w(r:=n%10**e)+(0<r<100)or(n>0)+(n>20)
g=lambda k:k and g(k//3)*10+k%3
L=1
while 1:
 k=1
 while w(g(k))-L:k+=1
 print(g(k));L+=1
