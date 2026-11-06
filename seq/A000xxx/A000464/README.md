# A000464

> Expansion of e.g.f. sin(x)/cos(2*x).
> — [OEIS A000464](https://oeis.org/A000464)

Offset 0: 1, 11, 361, 24611, 2873041, 512343611, 129570724921, 44110959165011, 19450718635716001, 10784052561125704811, …

### Python 3 — 123 bytes

```python
from math import*
a=[]
while 1:
 n=len(a);a+=[(-1)**n-sum(comb(2*n+1,2*k)*(-4)**k*a[-k]for k in range(1,n+1))];print(a[-1])
```

**How it works**

Multiply the exponential generating function by its denominator:
cos(2x)*F(x)=sin(x). Equating derivatives gives the binomial
convolution in the program. The denominator has constant term 1,
so the new derivative is its numerator derivative minus the
contributions of all earlier derivatives. Odd or even indices
are selected by the 2*n+offset expression, matching the OEIS e.g.f.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 216 terms in 60 s; the official b-file contains 216 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 123 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000464), CC BY-SA 4.0.
