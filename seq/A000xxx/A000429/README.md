# A000429

> Number of n-node rooted trees of height 8.
> — [OEIS A000429](https://oeis.org/A000429)

Offset 1: 0, 0, 0, 0, 0, 0, 0, 0, 1, 8, …

### Python 3 — 123 bytes

```python
L=[1]*7;n=0
while[print(L[-7]-L[-6])]:
 n-=7
 for h in[1]*6+[0]:L+=sum(d*L[n-d-6]**h*sum(L[d::d])for d in range(n,0,7))//n,
```

**How it works**

- Let b_h(m) be the number of unlabelled rooted trees with m + 1 nodes and
  height at most h (in edges). Removing the root leaves a multiset of trees
  of height at most h − 1, so Σ_m b_h(m)xᵐ = Π_{k≥1} (1 − x^k)^(−b_{h−1}(k−1)),
  and logarithmic differentiation gives

  m·b_h(m) = Σ_{k=1}^{m} k·b_{h−1}(k−1)·Σ_{j≥1} b_h(m − jk),

  with b_1(m) = 1 (the star). a(n) = b_8(n−1) − b_7(n−1).
- One list holds the layers in rows of 7: b_8(m), b_7(m), …, b_2(m) for
  m = 0, 1, …; every b_h(0) is 1. When row m is built, n = −7m and the
  generator variable is d = −7k, so for the column being appended the slice
  `L[d::d]` steps back 7k places at a time from the end, through
  b_h(m−k), b_h(m−2k), … of the same column.
- The weight b_{h−1}(k−1) sits in the next column of row k − 1. Counted from
  the end of the list it is at index −7(m−k) − 6 = `n-d-6` whatever column is
  being appended, because the list grows by one entry per column. For the
  last column (h = 2) the weight is b_1 = 1, and `**h` with h = 0 makes it 1;
  the other six passes have h = 1.
- d and n carry the same factor −7, which cancels in `//n`; the division is
  exact by the identity. `L[-7]-L[-6]` is b_8(m) − b_7(m), the trees of
  height exactly 8 with m + 1 nodes.

**Notes**

- `for h in range(7):` with the weight `L[(-d-6+h)*(h<6)]` (a positive index,
  0 for the last column, where L[0] = 1): 129 bytes. `for h in
  1,1,1,1,1,1,0:` costs 5 bytes more than `[1]*6+[0]`.
  [A000342](../A000342/) (height 5) uses the same template;
  [A000418](../A000418/) (height 7) has the same structure in rows of 6.
- Exact integer arithmetic, so the program is right for every n. A path needs
  9 nodes to reach height 8, hence the eight leading zeros.
- About 1980 terms in 60 s here.
- The b-file has 200 terms (up to a(200)); the bar is the whole b-file in
  60 s.
- The terms grow by a factor below 2.96 (Otter's constant) per node, so the
  4300-digit int-to-str limit lies beyond n = 9000, out of reach in practice.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 129 | first entry |
| 2026-11-07 | Python 3 | 123 | weight index `n-d-6` from the end, `**h` for the bottom layer |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000429), CC BY-SA 4.0.
