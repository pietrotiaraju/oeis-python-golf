# A000555

> Number of labeled trees of diameter 4 with n nodes.
> — [OEIS A000555](https://oeis.org/A000555)

Offset 5: 60, 720, 6090, 47040, 363384, 2913120, 24560910, 218386080, 2044958916, 20112075984, …

### Python 3 — 85 bytes

```python
m=4
while[print(-~m*sum(((2**m+1)**m>>m*k)%2**m*(k**(m-k)-k)for k in range(m)))]:m+=1
```

**How it works**

- **The count.** A tree of diameter 4 has a central node c, the middle of
  every longest path. Rooted at c it has height exactly 2, and at least two
  children of c have children of their own; conversely every such rooted
  tree has diameter 4 with c in the middle. With m = n − 1 labels besides c,
  rooted trees of height at most 2 with k children of c number
  C(m, k)·k^(m−k), as in [A000551](../A000551/). From their total remove
  the one of height 1 (k = m) and the m·(2^(m−1) − 1) where exactly one child
  w of c has children (each other label is a child of c or of w, not all of
  c). Since Σ_{k<m} C(m, k)·k = m·2^(m−1) − m, this is

  a(n) = n · Σ_{k=0}^{m−1} C(m, k)·(k^(m−k) − k).

  `-~m` is m + 1 = n, `range(m)` stops before k = m, and k = 0 gives 0.
- **Binomials without `math`.** `((2**m+1)**m>>m*k)%2**m` is C(m, k): the
  base-2^m digits of (2^m + 1)^m are the binomials C(m, j), all below 2^m
  for m ≥ 1 because they add up to 2^m. `%` and `*` group from the left, so
  `*(k**(m-k)-k)` follows without more parentheses.

**Notes**

- Other versions: `import math` with `math.comb(m,k)` is 88 bytes; the first
  entry, n·(Σ C(n − 1, k)·k^(n−1−k) − (n − 1)(2^(n−2) − 1) − 1), was 111.
- Exact integer arithmetic, so the program is right for every n.
- The whole b-file prints in about 0.1 s here, and about 320 terms in 60 s
  (a(325) has 546 digits, far from the 4300-digit int-to-str limit). The
  b-file has 24 terms (up to a(28)); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 111 | first entry |
| 2026-11-07 | Python 3 | 85 | single sum with C(m, k)·(k^(m−k) − k), binomials read from (2^m + 1)^m |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000555), CC BY-SA 4.0.
