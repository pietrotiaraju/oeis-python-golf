n=1;s={1};t={2};k=2
while 1:
 if n==k*k:s.add(n);t|={n+x for x in s};k+=1
 if n not in s and n not in t and any(n-x in t for x in s):print(n)
 n+=1
