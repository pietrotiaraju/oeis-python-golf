f=lambda c:c<{0}or sum(f(c-{j})*B**((j+len(c))%n<3)for j in c)
n=3
while n:=n+1:B=n**n;print(f({*range(n)})//B**2%B)