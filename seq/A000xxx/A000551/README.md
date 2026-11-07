# A000551

> Number of labeled rooted trees of height 2 with n nodes.
> — [OEIS A000551](https://oeis.org/A000551)

Offset 3: 6, 36, 200, 1170, 7392, 50568, 372528, 2936070, 24617120, 218521116, …

### Python 3 — 81 bytes

```python
m=2
while[print(-~m*sum(((2**m+1)**m>>m*k)%2**m*k**(m-k)for k in range(m)))]:m+=1
```

**How it works**

- **The count.** Pick the root (n ways) and its k children among the other
  m = n − 1 labels (C(m, k) ways); every remaining label hangs from one of
  the children (k^(m−k) ways). That gives the trees of height at most 2 with
  a root of degree k, so

  a(n) = n · Σ_{k=0}^{m−1} C(m, k)·k^(m−k).

  The term k = m (all labels are children: height 1) is left out by
  `range(m)`, and k = 0 contributes 0^m = 0. Every other term has a label
  at depth 2, so the height is exactly 2. `-~m` is m + 1 = n, and the loop
  starts at m = 2, that is n = 3.
- **Binomials without `math`.** By the binomial theorem
  (2^m + 1)^m = Σ_j C(m, j)·2^(mj), and every C(m, j) is below 2^m for
  m ≥ 1 (they add up to 2^m, with C(m, 0) = C(m, m) = 1 among them). So the
  base-2^m digits of (2^m + 1)^m are exactly the binomials, and
  `((2**m+1)**m>>m*k)%2**m` is C(m, k). `%` and `*` have the same precedence
  and group from the left, so the following `*k**(m-k)` needs no parentheses.

**Notes**

- Other versions: `import math` with `math.comb(m,k)` is 84 bytes; the first
  entry, n(n − 1)·Σ C(n − 2, k − 1)·k^(n−2−k) with `from math import*`, was 99.
- Exact integer arithmetic, so the program is right for every n.
- Each term rebuilds (2^m + 1)^m (m² bits) once per k: the whole b-file
  prints in about 3.6 s here, and about 330 terms in 60 s. The b-file has 198
  terms (up to a(200)); the bar is the whole b-file in 60 s.
- a(n) has about n·log₁₀(n/ln n) digits (564 at the 330th term), so the
  4300-digit int-to-str limit is far beyond what a minute reaches.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 99 | first entry; direct count by root degree |
| 2026-11-07 | Python 3 | 81 | sum over C(n−1, k) with binomials read from (2^m + 1)^m |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000551), CC BY-SA 4.0.
