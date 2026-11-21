L=[1];T={2,4};m=1;r=0
while m:=m+2:
 if all(m%p for p in L[1:1<<m.bit_length()//2]):L+=m,;T|={2*m}
 if(q:=next((q for q in L if m-q in T),0))>r:r=q;print(m)
