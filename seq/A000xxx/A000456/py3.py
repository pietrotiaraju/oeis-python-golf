A=[1];B=[1];n=0
while n:=n+1:
 for a,q in(A,5),(B,6):c=1;a+=[sum((c:=c*(n-k+1)//k)*(k%q<2)*(k%q*2-1)*a[-k]for k in range(1,n+1))]
 print(B[-1]-A[-1])
