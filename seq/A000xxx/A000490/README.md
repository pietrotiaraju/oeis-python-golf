# A000490

> Generalized Euler numbers c(4,n).
> — [OEIS A000490](https://oeis.org/A000490)

Offset 0: 1, 16, 1280, 249856, 90767360, 52975108096, 45344872202240, 53515555843342336, 83285910482761809920, 165262072909347030040576, …

### Python 3 — 115 bytes

```python
from math import*
a=[1]
while[print(a[-1])]:
 n=len(a);a+=[-sum(comb(2*n,2*k)*(-16)**k*a[-k]for k in range(1,n+1))]
```

**How it works**

The e.g.f. is sec(4x). Multiply by cos(4x) and equate the
2n-th derivatives: a(0)=1 and
a(n)=-sum(C(2n,2k)*(-16)^k*a(n-k),k=1..n).
The list stores the preceding derivatives, so `a[-k]` is a(n-k).

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 195 terms in 60 s; the official b-file contains 195 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 115 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000490), CC BY-SA 4.0.
