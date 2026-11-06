n=5
while[N:=n*n,print(sum((q:=(N+z-x-y)**2-4*x*y-4*N*z)*abs(q)>=64*N*x*y*z for z in range(N)for y in range(z)for x in range(1,y)))]:n+=1