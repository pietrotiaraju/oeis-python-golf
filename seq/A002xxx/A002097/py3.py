n=0
while 1:n+=1;R=range(1,n);all(a*~a+b*~b+c*~c+2*n for a in R for b in R for c in R)and print(n)
