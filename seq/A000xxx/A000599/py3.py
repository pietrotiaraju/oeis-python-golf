A=[1];C=[];n=0
print(0)
while 1:
 C+=sum(A[j]*A[n-j]for j in range(n+1)),
 A+=(sum(C[j]*A[n-j]for j in range(n+1))+3*sum(A[j]*A[n-2*j]for j in range(n//2+1))+2*(n%3<1)*A[n//3])//6,
 print((C[n]+(n%2<1)*A[n//2])//2-A[n]);n+=1
