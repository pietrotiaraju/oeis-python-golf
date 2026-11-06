# A000411

> Generalized tangent numbers d(6,n).
> — [OEIS A000411](https://oeis.org/A000411)

Offset 1: 6, 522, 152166, 93241002, 97949265606, 157201459863882, 357802951084619046, 1096291279711115037162, 4350684698032741048452486, 21709332137467778453687752842, …

### Python 3 — 128 bytes

```python
from math import*
a=[]
while 1:
 n=len(a);a+=[6*(-9)**n-2*sum(comb(2*n+1,2*k)*(-16)**k*a[-k]for k in range(1,n+1))];print(a[-1])
```

**How it works**

Multiply the exponential generating function by its denominator:
(2*cos(4x)-1)*F(x)=2*sin(3x). Equating derivatives gives the binomial
convolution in the program. The denominator has constant term 1,
so the new derivative is its numerator derivative minus the
contributions of all earlier derivatives. Odd or even indices
are selected by the 2*n+offset expression, matching the OEIS e.g.f.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 184 terms in 60 s; the official b-file contains 184 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 128 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000411), CC BY-SA 4.0.
