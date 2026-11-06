# A000266

> Expansion of e.g.f. exp(-x^2/2) / (1-x).
> — [OEIS A000266](https://oeis.org/A000266)

Offset 0: 1, 1, 1, 3, 15, 75, 435, 3045, 24465, 220185, …

a(n) is the number of permutations of n letters with no 2-cycle.

### Python 3 — 48 bytes

```python
a=b=c=n=1
while 1:b,c=c,n*b;n-=1;print(a:=c-a*n)
```

**How it works**

- Write the e.g.f. as A = B/(1 − x) with B = exp(−x²/2). Then
  (1 − x)·A = B, which coefficient by coefficient says
  a(n) = n·a(n−1) + b(n), where b(n) = n!·[xⁿ] B. From B′ = −x·B,
  b(n) = −(n−1)·b(n−2) with b(0) = 1, b(1) = 0, so b(2m) = (−1)^m·(2m−1)!!
  and every odd b is 0.
- `n` runs through the negated index, `n` = −N, so the minus sign in both
  recurrences is free. `b, c` hold b(N−1), b(N): the swap `b,c=c,n*b` moves
  them to b(N), b(N+1) = −N·b(N−1). After `n-=1`, a(N+1) = (N+1)·a(N) +
  b(N+1) is `c-a*n`.
- The loop starts one step early, at the phantom index N = −1 (`n=1`). The
  first pass makes b(0) = 1·b, so `b=1`; the old `c` and `a` are only ever
  multiplied by the next `n`, which is 0, so they can be anything. All four
  variables start at 1, and printing at the end of the loop body (instead of
  `while[print(a)]:`) keeps the phantom term from being printed.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (451 terms) prints at once, and all 1559 terms it prints match
  n!·Σ_{k≤n/2} (−1)^k/(k!·2^k) (checked exactly for n < 300, and against
  the b-file); it stops after a(1558), when a(1559) passes the 4300-digit
  int-to-str limit of Python 3.11+. The bar is the whole b-file in 60 s.
- The print can also go in the loop header,
  `while[print(a:=c-a*n)]:b,c=c,n*b;n-=1`, one byte shorter, but then the
  first header already prints, so there is no phantom step and the start is
  `a=b=c=1;n=0` (49 bytes).
- Three numbers are really needed: b has zeros at every odd n, so it has no
  first-order recurrence, and a itself has order 3
  (a(n) = n·a(n−1) − (n−1)·a(n−2) + (n−1)(n−2)·a(n−3)). Keeping only the
  nonzero b in one variable needs a parity test, which costs more than the
  swap.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000266), CC BY-SA 4.0.
