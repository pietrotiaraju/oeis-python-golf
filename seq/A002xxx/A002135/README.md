# A002135

> Number of terms in a symmetrical determinant: a(n) = n*a(n-1) - (n-1)*(n-2)*a(n-3)/2.
> — [OEIS A002135](https://oeis.org/A002135)

Offset 0: 1, 1, 2, 5, 17, 73, 388, 2461, 18155, 152531, 1436714, 14986879, …

### Python 3 — 59 bytes

```python
x=y=m=0;z=1
while[print(z)]:x,y,z=y,z,-~m*z-m*~-m*x//2;m+=1
```

**How it works**

- **Recurrence.** The name is the recurrence
  a(n) = n·a(n−1) − (n−1)(n−2)/2·a(n−3) with a(0) = a(1) = 1, a(2) = 2
  (Comtet; equivalently, the e.g.f. (1−x)^(−1/2)·exp(x/2 + x²/4) has
  log-derivative (2 − x²)/(2(1 − x)), so 2(1−x)F′ = (2 − x²)F).
- **Phantom start.** With a(−1) = a(−2) = 0 the same recurrence gives
  a(1) = 1·a(0) = 1 and a(2) = 2·a(1) − 0 = 2, so the state
  (x, y, z) = (a(m−2), a(m−1), a(m)) starts at (0, 0, 1) and the two extra
  initial values cost nothing.
- **Loop.** With m = n − 1 the new term is (m+1)·z − C(m, 2)·x:
  `-~m*z` is (m+1)·z, and `m*~-m*x//2` is m(m−1)·x/2, exact because
  m(m−1) is even.

**Notes**

- a(n) is also the number of ways to deal a deck with two cards of each of
  n kinds into n two-card hands, and the number of ways to cover n labeled
  points by disjoint undirected cycles, loops and double edges included
  (comments in the entry).
- a(n) has about n·log₁₀ n digits; the b-file has 101 terms (n = 0 to
  100), and the bar is the whole b-file in 60 s, which takes a fraction of
  a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 59 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002135), CC BY-SA 4.0.
