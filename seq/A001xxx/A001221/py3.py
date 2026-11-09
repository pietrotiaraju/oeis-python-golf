P=n=1;L=[]
while[print(sum(n%p<1for p in L))]:P*=n*n;n+=1;L+=P%n*[n]
