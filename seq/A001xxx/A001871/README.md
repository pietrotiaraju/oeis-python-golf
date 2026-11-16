# A001871

> Expansion of 1/(1 - 3*x + x^2)^2.
> — [OEIS A001871](https://oeis.org/A001871)

Offset 0: 1, 6, 25, 90, 300, 954, 2939, 8850, 26195, 76500, 221016, …

### Python 3 — 47 bytes

```python
q=d=e=g=1
while[print(q)]:e+=g;g+=e;d+=q+g;q+=d
```

**How it works**

- G = 1/(1 − 3x + x²) = Σ F(2n + 2)·xⁿ, the even-indexed Fibonacci numbers,
  and the sequence is G², so (1 − 3x + x²)·G² = G gives
  q(n) = 3q(n−1) − q(n−2) + F(2n + 2), with q(−1) = 0, q(0) = 1.
- `e`, `g` hold F(2n + 1), F(2n + 2); `e+=g;g+=e` takes two Fibonacci steps,
  so `g` becomes F(2n + 4) for the next term.
- Instead of q(n−1) the program keeps the difference d(n) = q(n) − q(n−1).
  The recurrence becomes d(n) = q(n−1) + d(n−1) + F(2n + 2), then
  q(n) = q(n−1) + d(n): `d+=q+g;q+=d`, two short in-place updates instead
  of a tuple assignment with 3·q.
- All four start at 1: q(0) = 1, d(0) = q(0) − q(−1) = 1, F(1) = F(2) = 1.
- d is (1 − x)·G², which is [A001870](../A001870/): the same program prints
  `d` there.

**Notes**

- With tuples, `f,g=g,3*g-f;p,q=q,3*q-p+g`, it is 53 bytes; the
  P-recurrence n·a(n) = 3(n + 1)·a(n−1) − (n + 2)·a(n−2) is 55.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole
  b-file in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001871), CC BY-SA 4.0.
