M=0,1;a=b=m=1
while[print(M[m])]:
 m+=1
 if m>b:a,b=b,a+b
 M+=M[-a]+M[b-m],
