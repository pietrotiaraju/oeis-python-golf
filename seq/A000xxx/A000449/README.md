# A000449

> Rencontres numbers: number of permutations of [n] with exactly 3 fixed points.
> — [OEIS A000449](https://oeis.org/A000449)

Offset 3: 1, 0, 10, 40, 315, 2464, 22260, 222480, 2447445, 29369120, …

### Python 3 — 51 bytes

```python
a=c=1;n=3
while[print(a)]:n+=1;c=c*n//(3-n);a=a*n+c
```

**How it works**

- Choose the 3 fixed points and derange the other n − 3 elements:
  a(n) = C(n, 3)·D(n−3), with D the derangement numbers
  [A000166](../A000166/).
- D(m) = m·D(m−1) + (−1)ᵐ and (n−3)·C(n, 3) = n·C(n−1, 3) give
  a(n) = n·a(n−1) + (−1)^(n−3)·C(n, 3) = n·a(n−1) − (−1)ⁿ·C(n, 3),
  starting from a(3) = 1.
- `c` carries the signed binomial −(−1)ⁿ·C(n, 3), which is 1 at n = 3, so
  the update is a plain `a=a*n+c`. The step C(n, 3) = C(n−1, 3)·n/(n−3)
  becomes `c=c*n//(3-n)`: dividing by 3 − n instead of n − 3 flips the
  sign for free, and the floor division is exact because the quotient is
  ±C(n, 3), an integer (the [A000475](../A000475/) trick).
- `while[print(a)]:` prints first in every pass, so a(3) = 1 comes out
  before the first step.

**Notes**

- Measured alternatives: C(m+3, 3)·D(m) with m = n − 3, D by the
  start-early walrus `d:=d*m^1` (m·D(m−1) has the parity of m, so adding
  (−1)ᵐ is `^1`) and `c=c*(m+3)//m`, 54 bytes, or with C(m+3, 3) built by
  running sums (`b-=~m;c+=b`), also 54; the recurrence with the sign and
  binomial written out, `a=n*a-(-1)**n*n*(n-1)*(n-2)//6`, 59.
- Exact integer arithmetic, so the program is right for every n.
- The whole b-file prints at once. The b-file has 98 terms (up to
  a(100)); the bar is the whole b-file in 60 s.
- a(1558) has 4299 digits and a(1559) more than 4300, so the int-to-str
  limit stops the printing after a(1558).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 59 | first entry |
| 2026-11-07 | Python 3 | 54 | C(m+3,3)·D(m) with the start-early `d*m^1` walrus |
| 2026-11-07 | Python 3 | 51 | signed binomial step `c*n//(3-n)` in a(n) = n·a(n−1) − (−1)ⁿC(n,3) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000449), CC BY-SA 4.0.
