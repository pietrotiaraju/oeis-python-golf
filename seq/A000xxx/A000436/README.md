# A000436

> Generalized Euler numbers c(3,n).
> — [OEIS A000436](https://oeis.org/A000436)

Offset 0: 1, 8, 352, 38528, 7869952, 2583554048, 1243925143552, 825787662368768, 722906928498737152, 806875574817679474688, …

### Python 3 — 123 bytes

```python
from math import*
a=[]
while 1:
 n=len(a);a+=[(-1)**n-sum(comb(2*n+0,2*k)*(-9)**k*a[-k]for k in range(1,n+1))];print(a[-1])
```

**How it works**

Multiply the exponential generating function by its denominator:
cos(3x)*F(x)=cos(x). Equating derivatives gives the binomial
convolution in the program. The denominator has constant term 1,
so the new derivative is its numerator derivative minus the
contributions of all earlier derivatives. Odd or even indices
are selected by the 2*n+offset expression, matching the OEIS e.g.f.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 101 terms in 60 s; the official b-file contains 101 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 123 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000436), CC BY-SA 4.0.
