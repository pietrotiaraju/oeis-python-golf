f=lambda L,k,y:k and max(f([q:=s|q<<a for s in L],k-1,len(bin(q^q+1)))for a in range(y)if[q:=0])or y-4
n=0
while 1:n+=1;v=2*n//9;q=4*-~n//9;a=2*q-v+3;print(n<23and f([1]*-~n,3,4)or(n-v-q)*((v+2)*a-q-2)+v*a+q)
