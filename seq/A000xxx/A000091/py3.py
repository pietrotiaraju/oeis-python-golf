n=0
while R:=range(n:=n+1):print(sum(x*x%n==x for x in R)*any((x*x+3<<n)%n<1for x in R))
