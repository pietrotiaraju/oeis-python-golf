n=1;s={1};k=2
while 1:
 if n==k*k:s.add(n);k+=1
 if n not in s and any(n-x in s for x in s):print(n)
 n+=1
