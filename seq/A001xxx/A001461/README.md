# A001461

> Partial sums of A006206.
> — [OEIS A001461](https://oeis.org/A001461)

Offset 1: 1, 2, 3, 4, 6, 8, 12, 17, 25, 36, 54, 79, 119, 177, 267, 402, 612, 928, 1420, …

### Python 3 — 103 bytes

```python
b=[0,1];n=x=1;y=3
while[print(sum(b))]:n+=1;b+=(y-sum(d*b[d]for d in range(1,n)if n%d<1))//n,;x,y=y,x+y
```

**How it works**

- [A006206](https://oeis.org/A006206)(m) = b(m) counts the aperiodic binary
  necklaces of length m with no two adjacent 0s, and the OEIS gives
  b(m) = (1/m)·Σ_{d|m} μ(m/d)·L(d) with L the Lucas numbers
  [A000204](../A000204/) (L(1) = 1, L(2) = 3, L(m) = L(m−1) + L(m−2)).
  By Möbius inversion this is the same as **L(m) = Σ_{d|m} d·b(d)** for
  every m (also stated there), so b(m) = (L(m) − Σ_{d|m, d<m} d·b(d))/m: no Möbius function
  is needed, and the division is exact because b(m) is an integer.
- The list `b` holds b(0) = 0 (a placeholder, so that `b[d]` is b(d)),
  b(1), b(2), …; the term a(n) = b(1) + … + b(n) is just `sum(b)`.
  `x`, `y` are L(n−1), L(n) and move on with `x,y=y,x+y`.
- The start is the state after n = 1: b(1) = 1, x = L(1) = 1 and
  y = L(2) = 3, and `n+=1` comes first in the loop, so `y` is L(n) when
  b(n) is computed.

**Notes**

- The same divisor-sum inversion as the binary Lyndon words of
  [A001037](../A001037/) and their partial sums [A001036](../A001036/),
  with L(m) in place of 2^m; there the 2^m is a closed form, here the
  Lucas pair is shorter than any exact closed form (a lambda `g` reading a
  list of Lucas numbers is 114 bytes).
- Keeping c(m) = m·b(m) instead and a running sum `s+=c[n]//n` is
  104 bytes.
- Exact integer arithmetic, so the program is right for every n. Term n
  scans all d < n, so the first N terms take about N²/2 steps: the whole
  b-file (1000 terms) prints in about 0.2 s, and that is the bar. a(n) has
  about 0.209·n digits, so the 4300-digit int-to-str limit would only be
  reached near n = 20600.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 103 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001461), CC BY-SA 4.0.
