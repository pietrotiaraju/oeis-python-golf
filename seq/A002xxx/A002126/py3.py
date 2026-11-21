z=[1];P=n=1
while[print(sum(map(min,z,z[::-1])))]:z+=P%n,;P*=n*n;n+=1
