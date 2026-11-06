g=lambda t,i=0:t<1or i*i<=t%m<t and g(t-i*i-m,i)+g(t,i+1)
m=1
while[print(g(6*m-1))]:m+=1
