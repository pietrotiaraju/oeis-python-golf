# A001870

> Expansion of (1-x)/(1 - 3*x + x^2)^2.
> — [OEIS A001870](https://oeis.org/A001870)

Offset 0: 1, 5, 19, 65, 210, 654, 1985, 5911, 17345, 50305, 144516, …

### Python 3 — 47 bytes

```python
q=d=e=g=1
while[print(d)]:e+=g;g+=e;d+=q+g;q+=d
```

**How it works**

- G = 1/(1 − 3x + x²) = Σ F(2n + 2)·xⁿ, the even-indexed Fibonacci numbers.
  The sequence is (1 − x)·G², the first differences d(n) = q(n) − q(n−1) of
  q = G² = [A001871](../A001871/).
- (1 − 3x + x²)·G² = G gives q(n) = 3q(n−1) − q(n−2) + F(2n + 2), with
  q(−1) = 0, q(0) = 1. Subtracting q(n−1):
  d(n) = q(n−1) + d(n−1) + F(2n + 2), and then q(n) = q(n−1) + d(n). That
  is `d+=q+g;q+=d`.
- `e`, `g` hold F(2n + 1), F(2n + 2); `e+=g;g+=e` takes two Fibonacci steps,
  so `g` becomes F(2n + 4) for the next term.
- All four start at 1: d(0) = q(0) = 1 (as q(−1) = 0), F(1) = F(2) = 1. The
  same program prints `q` for A001871.

**Notes**

- Printing `b-a` from the P-recurrence of A001871 is 57 bytes; the tuple
  version `p=0;q=f=g=1` … `f,g=g,3*g-f;p,q=q,3*q-p+g` is 53.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole
  b-file in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001870), CC BY-SA 4.0.
