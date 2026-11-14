# A001708

> Generalized Stirling numbers, [n+6,6]_2.
> — [OEIS A001708](https://oeis.org/A001708)

Offset 0: 1, 20, 295, 4025, 54649, 761166, 11028590, 167310220, 2664929476, 44601786944, 784146622896, …

### Python 3 — 68 bytes

```python
import math
s=4
while[print(math.perm((B:=s**s)-~s,s)//B**4%B)]:s+=1
```

**How it works**

- The generalized Stirling number [N, K]ᵣ (Mitrinović's numbers with a = −r, b = −1, as in the entry; the r-Stirling numbers of the first kind) is the coefficient of x^K in xʳ(x+r)(x+r+1)⋯(x+N−1). Here r = 2 and K = j + 2 with j = 4, so a(n) is the coefficient
  of x⁴ in P(x) = (x+2)(x+3)⋯(x+s+1) with s = n + 4 (s factors).
- `math.perm(N, k)` is the falling product N(N−1)⋯(N−k+1), so
  `math.perm(B-~s,s)` = (B+s+1)(B+s)⋯(B+2) = P(B) (`-~s` is s + 1).
- In base B = sˢ the coefficients of P are the digits of P(B), because each
  is less than B. For s ≥ 5 their sum P(1) = (s+2)!/2 is already below sˢ:
  2520 < 3125 at s = 5, and from s to s + 1 the left side grows by the factor
  s + 3, the right side by (s+1)(1+1/s)ˢ ≥ 2(s+1). At s = 4 the coefficients 120, 154, 71, 14, 1 are below 256.
  So `//B**4%B` reads the coefficient of x⁴. The walrus defines B
  inside the first argument; s starts at 4 for a(0) = 1.

**Notes**

- Exact integer arithmetic, correct for every n. It prints up to a(1552); the next term passes the 4300-digit int-to-str limit of Python 3.11+ and stops it. The whole b-file (101 terms, n = 0 to 100) prints in well under a second; the bar is the whole b-file in 60 s.
- Keeping one variable per coefficient, as in [A001707](../A001707/), costs
  more as the power grows. The diagonal U(n, k) = [xᵏ] of the first n + k
  factors obeys U(n, k) = (r+n+k−1)·U(n−1, k) + U(n, k−1) with U(0, k) = 1, a
  running sum in a list (`q=[1]*5;c=5` /
  `while[print(q[4])]:s=0;c-=4;q=[s:=(c:=c+1)*v+s for v in q]`), 70 bytes.
- `math.perm((B:=s**s)+s,s-1)` (top factor B + s, so s = n + 5) is a byte longer.
- Same template as [A001233](../A001233/) (Stirling numbers, r = 1); also
  [A001709](../A001709/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001708), CC BY-SA 4.0.
