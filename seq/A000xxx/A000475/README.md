# A000475

> Rencontres numbers: number of permutations of [n] with exactly 4 fixed points.
> — [OEIS A000475](https://oeis.org/A000475)

Offset 4: 1, 0, 15, 70, 630, 5544, 55650, 611820, 7342335, 95449640, …

### Python 3 — 70 bytes

```python
from math import*
a=1;n=4
while[print(a)]:n+=1;a=n*a+(-1)**n*comb(n,4)
```

**How it works**

Rencontres numbers with four fixed points are C(n,4)*D(n-4).
The derangement recurrence gives a(n)=n*a(n-1)+(-1)^n*C(n,4),
starting with a(4)=1; every operation is an integer operation.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 97 terms in 60 s; the official b-file contains 97 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000475), CC BY-SA 4.0.
