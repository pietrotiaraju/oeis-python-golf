# A000450

> a(n) = A058057(n,n-4).
> — [OEIS A000450](https://oeis.org/A000450)

Offset 4: 1, 10, 50, 385, 3130, 28764, 291900, 3249210, 39367395, 515874470, …

### Python 3 — 114 bytes

```python
from math import*
n=4
while 1:print(sum((-1)**k*factorial(n-k)*comb(k,4)*comb(2*n-k,k)for k in range(4,n+1)));n+=1
```

**How it works**

Take the coefficient of t⁴ in the straight-table ménage hit
polynomial sum(C(2n-k,k)*(n-k)!*(t-1)^k,k=0..n).
The coefficient is (-1)^(k-4)*C(k,4), producing the finite
inclusion-exclusion sum stated by the OEIS. Printing starts at n=4.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 447 terms in 60 s; the official b-file contains 447 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 114 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000450), CC BY-SA 4.0.
