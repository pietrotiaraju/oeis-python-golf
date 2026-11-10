P=n=1;S={0}
while 1:[print(x)for x in range(P%n*n)if n-x*x in S];P*=n*n;S|={3*n*n};n+=1
