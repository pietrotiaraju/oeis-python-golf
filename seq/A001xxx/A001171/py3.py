f=lambda n:n<1or-n*f(n-1)
k=0
while 1:k+=1;M=f(7*k);print(k*sum(M*(-8)**d*(4*d+2)*f(A:=B+d)**3*f(2*B)**2*f(m:=k+~A-B)*(m or B<1)//((d*d-k*k)*(k*k-~d*~d or 2*k)*f(A-~A)*f(B)**3)for B in range(k)for d in range(k-2*B))//M)
