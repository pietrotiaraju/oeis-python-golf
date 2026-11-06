n=1;s={1};t={2};u={3};k=2
while 1:
 if n==k*k:s.add(n);t|={n+x for x in s};u|={n+x for x in t};k+=1
 if any(n-x in u for x in s):print(n)
 n+=1
