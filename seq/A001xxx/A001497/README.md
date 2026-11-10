# A001497

> Triangle of coefficients of Bessel polynomials (exponents in decreasing order).
> — [OEIS A001497](https://oeis.org/A001497)

Offset 0: 1, 1, 1, 3, 3, 1, 15, 15, 6, 1, 105, 105, 45, 10, 1, 945, 945, 420, 105, …

### Python 3 — 79 bytes

```python
from math import*
n=k=0
while[print(comb(n+k,k)*perm(n,k)>>k)]:n+=k<1;k=~-k%-~n
```

**How it works**

- Row n is T(n,0), …, T(n,n) with T(n,k) = (2n−k)!/(2^(n−k)·k!·(n−k)!),
  the coefficients of the reversed Bessel polynomial θ_n(x) = xⁿ·y_n(1/x)
  (rows 1; 1, 1; 3, 3, 1; 15, 15, 6, 1; …).
- With j = n − k this is the [A001498](../A001498/) entry
  (n+j)!/(2^j·j!·(n−j)!) = C(n+j, j)·n!/(n−j)!/2^j, which is
  `comb(n+k,k)*perm(n,k)>>k` with `k` playing j. The shift is exact
  because the entry is an integer.
- So the row is A001498's row read backwards, and the walk does just
  that: `n+=k<1;k=~-k%-~n` steps j down by one, and after j = 0 it moves
  to the next row, where (−1) mod (n+1) = n starts it at j = n. The usual
  forward walk is `k=-~k%-~n;n+=k<1`; both are 16 bytes.

**Notes**

- The multiplicative row walk of A001498 (76 bytes there) would need
  T(n,0) = (2n−1)!! at the start of every row here, which costs more
  than it saves.
- Exact integer arithmetic, so the program is right for every n; the
  first entry over the 4300-digit int-to-str limit is T(1424, 0), the term
  with index 1014600 (counting from 0).
- The b-file has 1326 terms (rows 0 to 50); all of them print in well
  under a second, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001497), CC BY-SA 4.0.
