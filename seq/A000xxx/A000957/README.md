# A000957

> Fine's sequence (or Fine numbers): number of relations of valence >= 1 on an n-set; also number of ordered rooted trees with n nodes having root of even degree.
> — [OEIS A000957](https://oeis.org/A000957)

Offset 0: 0, 1, 0, 1, 2, 6, 18, 57, 186, 622, 2120, 7338, 25724, 91144, 325878, …

### Python 3 — 54 bytes

```python
a=0;c=m=1
while[print(a)]:a=-~c-a>>1;m+=1;c=4*c-6*c//m
```

**How it works**

- The entry's identity C(n) = 2a(n+1) + a(n) for n ≥ 1 (C = Catalan
  numbers, [A000108](../A000108/)) gives a(n+1) = (C(n) − a(n))/2. It
  follows from the g.f. F = c/(1 + c) with c = x·C(x), since c = x + c²
  turns F·(2 + x) = c + x, that is 2F/x + F = C(x) + 1.
- At n = 0 the identity fails (C(0) = 1 but 2a(1) + a(0) = 2), so the step
  is rounded **up**: `-~c-a>>1` is ⌊(C(n) − a(n) + 1)/2⌋. For n ≥ 1 the
  difference C(n) − a(n) = 2a(n+1) is even and the +1 changes nothing; at
  n = 0 it turns ½ into a(1) = 1. This costs 2 bytes and saves the
  `print(0);` a start at a(1) would need.
- The Catalan numbers run along as in [A000108](../A000108/): `m` is the
  index plus 2 after its increment and C(m−1) = 4C(m−2) − 6C(m−2)/m,
  an exact division.

**Notes**

- Exact integer arithmetic. Python's 4300-digit int-to-str limit stops the
  program after a(7153) (C(n) passes 4300 digits there), far beyond the
  b-file.
- The b-file has 1671 terms (a(0) to a(1670)); all of them print in about
  0.1 s, and the bar is the whole b-file.
- The D-finite recurrence 2n·a(n) = (7n − 12)a(n−1) + 2(2n − 3)a(n−2)
  (valid from n = 3) needs two seeds and a longer update.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000957), CC BY-SA 4.0.
