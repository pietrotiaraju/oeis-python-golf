f=lambda c:c<{0}or sum(f(c-{j})for j in c if(j+len(c))%n>2)
n=0
while n:=n+1:print(f({*range(n)}))
