# A002136

> Matrices with 2 rows.
> — [OEIS A002136](https://oeis.org/A002136)

Offset 3: 1, 2, 6, 23, 109, 618, 4096, 31133, 267219, 2557502, 27011734, …

### Python 3 — 60 bytes

```python
x=y=m=0;z=1
while[print(z)]:x,y,z=y,z,z-~m*z-m*~-m*x//2;m+=1
```

**How it works**

- **What is counted.** The name gives no definition. Joel B. Lewis's
  comment counts the ways to deal a deck of pairs plus two single cards
  into two-card hands (order of hands and of cards in a hand irrelevant).
  His example (6 deals of {1, 1, 2, 2, 3, 4}) is a(5), not a(3), and his
  own formula and Arndt's PARI program reproduce the data only with
  a(n) = deals of n − 3 pairs and two singles into n − 2 hands. The
  program follows the data, with that reading.
- **E.g.f.** A deal is a multigraph: one vertex per kind, one edge per
  hand, the paired kinds of degree 2 and the two singles of degree 1. The
  two singles are the ends of one path through k of the N = n − 3 paired
  kinds (k! orders), and the rest is a deal of pairs alone, counted by
  [A002135](../A002135/) with e.g.f. (1−x)^(−1/2)·exp(x/2 + x²/4). So
  f(N) = a(N+3) = Σ_k N!/(N−k)!·A002135(N−k), with e.g.f.
  F = (1−x)^(−3/2)·exp(x/2 + x²/4).
- **Recurrence.** F′/F = (4 − x²)/(2(1 − x)), so 2(1−x)F′ = (4 − x²)F,
  which on coefficients is f(m+1) = (m+2)·f(m) − C(m, 2)·f(m−2), the
  template of [A002135](../A002135/) with m+2 for m+1: `z-~m*z` is
  z + (m+1)·z. Phantom values f(−1) = f(−2) = 0 give f(1) = 2 and
  f(2) = 6 from f(0) = 1.

**Notes**

- The recurrence reproduces all 448 terms of the b-file (n = 3 to 450),
  and Lewis's a(n+1) = A002135(n) + n·A002135(n−1) + n(n−1)·a(n−1) holds
  with the same index shift by 2.
- a(n) has about n·log₁₀ n digits; the bar is the whole b-file in 60 s,
  which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 60 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002136), CC BY-SA 4.0.
