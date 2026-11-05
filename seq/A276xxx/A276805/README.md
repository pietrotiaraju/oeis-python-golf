# A276805

> a(n) = numerator((n^2 + 3*n + 2)/n^3).
> — [OEIS A276805](https://oeis.org/A276805)

Offset 1: 6, 3, 20, 15, 42, 7, 72, 45, 110, 33, 156, 91, 210, 30, 272, …

### Python 3 — 41 bytes

```python
m=3
while[print(~-m*m//min(m&-m,8))]:m+=1
```

**How it works**

- n² + 3n + 2 = (n + 1)(n + 2), and n + 1 shares no factor with n, so the
  fraction reduces only by gcd(n + 2, n³).
- With m = n + 2, n ≡ −2 (mod m), so n³ ≡ −8 and gcd(m, n³) = gcd(m, 8).
  Hence **a(n) = (m − 1)·m / gcd(m, 8)**, and the loop runs over m from 3.
- gcd(m, 8) is the lowest set bit of m, capped at 8: `min(m&-m,8)`.
- `~-m*m` is (m − 1)·m, and it is evaluated before `//`.
- `while[print(...)]:` prints in the loop condition (`[None]` is true) and
  saves a byte over `while 1:print(...);`.

**Notes**

- The same formula with `math.gcd` is 56 bytes; the direct
  `(k:=-~n*(n+2))//gcd(k,n**3)` is 68, and `Fraction(...).numerator` is 80.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A276805), CC BY-SA 4.0.
