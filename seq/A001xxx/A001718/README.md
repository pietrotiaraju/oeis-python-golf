# A001718

> Generalized Stirling numbers, [n+7,7]_4.
> — [OEIS A001718](https://oeis.org/A001718)

Offset 0: 1, 22, 355, 5265, 77224, 1155420, 17893196, 288843260, 4876196776, 86194186584, 1595481972864, …

### Python 3 — 69 bytes

```python
import math
s=6
while[print(math.perm((B:=s**s)+s,s-3)//B**3%B)]:s+=1
```

**How it works**

- The generalized Stirling number [N, K]ᵣ (Mitrinović's numbers with a = −r, b = −1, as in the entry; the r-Stirling numbers of the first kind) is the coefficient of x^K in xʳ(x+r)(x+r+1)⋯(x+N−1). Here r = 4 and K = j + 4 with j = 3, so a(n) is the
  coefficient of x³ in P(x) = (x+4)(x+5)⋯(x+s) with s = n + 6
  (n + 3 factors).
- `math.perm(N, k)` is the falling product N(N−1)⋯(N−k+1), so
  `math.perm(B+s,s-3)` = (B+s)(B+s−1)⋯(B+4) = P(B).
- The coefficients of P are nonnegative and add up to P(1) =
  5·6⋯(s+1), at most s − 2 factors each at most s + 1, so
  P(1) ≤ (s+1)ˢ⁻² < e·sˢ⁻² < sˢ = B. They are therefore the base-B digits of
  P(B), and `//B**3%B` reads the coefficient of x³. The walrus
  defines B inside the first argument; s starts at 6 for a(0) = 1.

**Notes**

- Exact integer arithmetic, correct for every n. It prints up to a(1551); the next term passes the 4300-digit int-to-str limit of Python 3.11+ and stops it. The whole b-file (101 terms, n = 0 to 100) prints in well under a second; the bar is the whole b-file in 60 s.
- Keeping one variable per coefficient, as in [A001707](../A001707/), costs
  more as the power grows. The diagonal U(n, k) = [xᵏ] of the first n + k
  factors obeys U(n, k) = (r+n+k−1)·U(n−1, k) + U(n, k−1) with U(0, k) = 1, a
  running sum in a list (`q=[1]*4;c=6` /
  `while[print(q[3])]:s=0;c-=3;q=[s:=(c:=c+1)*v+s for v in q]`), 70 bytes.
- The four-coefficient row form of [A001707](../A001707/) (start from (x+4)(x+5), multiply in x + c) is 69 bytes here.
- Same template as [A001233](../A001233/) (Stirling numbers, r = 1); also
  [A001719](../A001719/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 69 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001718), CC BY-SA 4.0.
