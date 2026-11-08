# A000987

> Number of stochastic matrices of integers.
> — [OEIS A000987](https://oeis.org/A000987)

Offset 0: 0, 1, 1, 2, 7, 32, 184, 1268, 10186, 93356, 960646, 10959452, …

### Python 3 — 74 bytes

```python
a=b=m=-2;c=d=0
while[print(d)]:m+=1;a,b,c,d=m*b,m*c,m*d,2*m*d-~-m*c-b+a//2
```

**What is counted**

- The terms are Gupta's γ(n) (Duke Math. J. 1968, in the entry's links):
  for n ≥ 2, the n×n symmetric matrices with nonnegative integer entries
  and all row sums 2 ([A000985](../A000985/)) whose first row is
  (1, 1, 0, …, 0). A brute-force count gives 1, 2, 7, 32, 184 for
  n = 2…6, the entry's terms. Gupta's relation (3.3),
  γ(n) = (n−2)γ(n−1) + S(n−2) with S = A000985, is the formula in the
  entry (Sean A. Irvine), with a(0) = 0 and a(1) = 1.

**How it works**

- With E the e.g.f. of a(n), the relation reads E″ = xE″ + S, so
  P = E″ = S/(1−x) = (1−x)^(−3/2) exp(x²/4 + x/(2(1−x))), with
  p(n) = a(n+2). Its logarithmic derivative gives
  2(1−x)²P′ = (4 − 2x − 2x² + x³)P.
- The states are kept factorial-scaled: `d` = p(n), `c` = n·p(n−1),
  `b` = n(n−1)p(n−2), `a` = n(n−1)(n−2)p(n−3). With `m` = n+1 the recurrence
  is p(m) = 2m·d − (m−1)c − b + a/2, and the next states are just `m*b`,
  `m*c`, `m*d`. `a` holds a product of three consecutive integers, so
  `a//2` is exact.
- The machine starts two steps early, at m = −2 with `d` = `c` = 0 and
  `a` = `b` = −2, so that it prints a(0) = 0 first. The step to m = −1 gives
  0 + 0 + 2 − 1 = 1 = a(1) and leaves `a` = 2, `b` = `c` = 0; the step to
  m = 0 gives 2/2 = 1 = p(0), and multiplying by m = 0 clears the other
  states, so from there on it runs exactly as from p(0) = 1. The same
  machine prints A000985 as `d-c`.

**Notes**

- Exact integer arithmetic; it rests on Gupta's relation and the e.g.f.
  of A000985.
- The program stops at Python's 4300-digit `int`-to-`str` limit after
  1553 terms (well under a second); the b-file has 446 terms and the bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 74 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000987), CC BY-SA 4.0.
