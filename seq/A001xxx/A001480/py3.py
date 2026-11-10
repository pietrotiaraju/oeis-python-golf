P=n=1;S={0}
while 1:[print(y)for y in range(P%n*n)if n-3*y*y in S];P*=n*n;S|={n*n};n+=1
