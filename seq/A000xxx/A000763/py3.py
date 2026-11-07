from math import*
c=lambda u,v:sum(comb(n,k)*u[k]*v[~k]for k in range(n+1))
Q=[];Y=A=[1];n=0
while 1:Q+=c(Y,Y),;Y=Y+[(4*(n+3)*c(Q,Y)-3*(n+2)*Q[n])//6];A+=c(Q,A),;n+=1;print(A[n])
