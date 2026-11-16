# A001863

> Normalized total height of rooted trees with n nodes.
> — [OEIS A001863](https://oeis.org/A001863)

Offset 1: 0, 1, 4, 26, 236, 2760, 39572, 672592, 13227804, 295579520, …

### Python 3 — 62 bytes

```python
s=0;n=1
while[print(s)]:
 n+=1
 for i in range(n-1):s=s*i+n**i
```

**How it works**

- The total height of a rooted tree is the sum of the distances of its
  nodes from the root. Riordan and Sloane (*J. Austral. Math. Soc.* 10
  (1969)) showed that over all rooted trees on n labeled nodes it adds up to
  n!·Σ_{k=0}^{n−2} nᵏ/k! ([A001864](../A001864/)); normalized by n(n−1),
  a(n) = (n−2)!·Σ_{k=0}^{n−2} nᵏ/k!, the formula on the OEIS page
  (n·[A000435](../../A000xxx/A000435/)(n) = n(n−1)·a(n)).
- With S(m) = Σ_{k=0}^{m} nᵏ·m!/k!, S(m) = m·S(m−1) + nᵐ and S(−1) = 0, so
  the loop `s=s*i+n**i` over i = 0…n−2 ends with s = S(n−2) = a(n), in
  integers.
- The first pass multiplies by i = 0, which wipes the previous n's value,
  so s needs no reset. At n = 1 the loop is empty and s = 0 = a(1) is
  printed; for each later n, `n+=1` comes first and the header prints it on
  the next pass.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The same loop gives [A001864](../A001864/) (times n(n−1)) and
  [A000435](../../A000xxx/A000435/) (times n − 1).
- The b-file has 385 terms (n = 1 to 385); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 62 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001863), CC BY-SA 4.0.
