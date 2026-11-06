s=set();n=p=1
while 1:
 p*=n*n;n+=1
 if p%n:s|={n,n*n}
 if n in s:print(n)
