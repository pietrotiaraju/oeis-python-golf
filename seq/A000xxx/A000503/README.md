# A000503

> a(n) = floor(tan(n)).
> — [OEIS A000503](https://oeis.org/A000503)

Offset 0: 0, 1, -3, -1, 1, -4, -1, 0, -7, -1, …

### Python 3 — 261 bytes

```python
n=0
while 1:
 c=d=p=1;s=k=0
 while 1:
  k+=1;d*=k;c*=k;s*=k;p*=n
  if k%2:s+=p*(-1)**(k//2)
  else:c+=p*(-1)**(k//2)
  e=2*p*n;t=k+1
  if k>2*n and c*c*t*t>e*e:
   q=[(s*t+i*e)//(c*t+j*e)for i in(-1,1)for j in(-1,1)]
   if min(q)==max(q):print(q[0]);break
 n+=1
```

**How it works**

- `c/d` and `s/d` are the real and imaginary parts of the Taylor sum
  for exp(i*n), with common denominator d=k!. Each new term multiplies
  the previous numerators by k and adds ±n^k to the appropriate one.
- For k>2n, the absolute sum of all omitted terms is at most
  2*n^(k+1)/(k+1)!. Thus `(c*t±e)/(d*t)` and `(s*t±e)/(d*t)` enclose
  cos(n) and sin(n), where t=k+1 and e=2*n^(k+1).
- `c*c*t*t>e*e` ensures the cosine interval excludes zero. A ratio over
  this rectangle attains its extrema at corners; if all four floors
  agree, that common integer is floor(tan(n)). Python's `//` handles
  negative values with the required floor convention.
- For n>0, cos(n) is nonzero and tan(n) is not an integer, by the
  transcendence of exp(2*i*n). The intervals therefore eventually decide
  every term. At n=0 the program prints 0.

**Notes**

- Exact integer interval arithmetic avoids the failures of `math.tan`
  near poles and at large arguments.
- Recomputing Taylor sums is expensive; the bar covers the first 100
  arguments, while all remaining terms use the same proven method.
- The reference file contains 1001 terms from the OEIS b-file; the verification
  bar is 100 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 261 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000503), CC BY-SA 4.0.
