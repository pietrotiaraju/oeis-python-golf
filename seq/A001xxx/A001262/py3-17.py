f=lambda e:pow(2,e,k)in{k-1,e%2or f(e//2)}
k=P=2
while[P%k<f(k-1)==print(k)]:P*=k;k+=1
