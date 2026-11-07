# A000588

> a(n) = 7*binomial(2n,n-3)/(n+4).
> — [OEIS A000588](https://oeis.org/A000588)

Offset 0: 0, 0, 0, 1, 7, 35, 154, 637, 2548, 9996, …

a(n) is the coefficient of x^(n−3) in C(x)⁷, the 7th power of the Catalan
generating function, and also the ballot number C(2n, n−3) − C(2n, n−4).

### Python 3 — 59 bytes

```python
import math
m=1
while[print(7*math.comb(m,m//2+4)//m)]:m+=2
```

**How it works**

- **The formula.** With m = 2n + 1, a(n) = 7·C(m, n+4)/m. This is the
  defining formula rewritten: C(2n+1, n−3) = C(2n, n−3)·(2n+1)/(n+4), and
  C(m, n+4) = C(m, n−3) by symmetry. It is also the power rule
  [x^j] C(x)^k = k/(2j+k)·C(2j+k, j) with k = 7, j = n − 3.
- **Exactness.** a(n) = C(2n, n−3) − C(2n, n−4), because
  C(2n, n−4) = C(2n, n−3)·(n−3)/(n+4) and 1 − (n−3)/(n+4) = 7/(n+4). So
  7·C(m, n+4) is m times an integer and `//m` is exact.
- **The zeros.** `m` steps through the odd numbers, and `m//2+4` is n + 4.
  For n = 0, 1, 2 the lower index n + 4 exceeds m = 2n + 1, where
  `math.comb` returns 0, so a(0) = a(1) = a(2) = 0 need no special case
  (`math.comb(2*n,n-3)` would raise an error there).
- `import math` plus `math.comb` is a byte shorter than `from math import*`
  plus `comb` when the function is used once.

**Notes**

- Other versions that print the same terms: `from math import*` with
  `comb`: 60 bytes; the loop over n,
  `while[print(7*math.comb(2*n,n+3)//(n+4))]:n+=1`: 62 bytes; the
  hypergeometric recurrence of [A000589](../A000589/) (54 bytes there) with
  the three zeros printed first, `print('0\n0\n0')`: 71 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 201 terms (up to a(200)) and all of them print at once; the
  bar is the whole b-file in 60 s.
- a(7151) is the first term with more than 4300 digits, so the int-to-str
  limit stops the program after a(7150), about 35 s in here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 77 | first entry |
| 2026-11-07 | Python 3 | 59 | C(2n+1, n+4)/(2n+1) over odd m: the zeros come from `math.comb` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000588), CC BY-SA 4.0.
