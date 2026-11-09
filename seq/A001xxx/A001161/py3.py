M=239585418511822
f=lambda n:n>99and f(n//10**(e:=~-len(str(n))//3*3or 2))+(M>>28+e//3)+f(n%10**e)or n>19and(M>>n//10+18)+f(n%10)or M>>n
n=0
while 1:f(n)%2or print(n);n+=1
