# A001268

> One-half the number of permutations of length n with exactly 4 rising or falling successions.
> — [OEIS A001268](https://oeis.org/A001268)

Offset 0: 0, 0, 0, 0, 0, 1, 11, 113, 1099, 11060, 118484, 1366134, 16970322, …

A succession is a position where neighbouring entries differ by 1, as in
1 2 or 4 3. Reversing a permutation keeps its successions and never gives
the same permutation back (n ≥ 2), so the permutations with exactly four
come in pairs and a(n) counts the pairs: column k = 4 of
[A001100](../A001100/), halved.

### Python 3 — 137 bytes

```python
from math import*
n=0
while[print(sum((-1)**m*comb(m,4)*perm(n-m)*comb(n-m,b+1)*comb(m-1,b)<<b for m in range(n)for b in range(m)))]:n+=1
```

**How it works**

- **At least m.** Let e(n, m) count the pairs (π, X): π a permutation
  of 1..n and X a set of m of its successions. Glue the pairs of X:
  each maximal chain of glued positions holds consecutive values in
  increasing or decreasing order. So a pair is the same as cutting the
  values 1..n into k = n − m intervals, choosing a direction for each
  interval of two or more values and an order of the k intervals. If b
  of the intervals are long, there are C(k, b) choices of which ones
  and C(m−1, b−1) ways to share the m extra values among them:
  e(n, m) = k!·Σ_b C(k, b)·C(m−1, b−1)·2ᵇ.
- **Exactly 4.** e(n, m) = Σ_π C(s(π), m), where s(π) is the number of
  successions, so binomial inversion gives the number with exactly j:
  Σ_m (−1)^(m−j)·C(m, j)·e(n, m).
- **The code.** With b − 1 in place of b, 2ᵇ = 2·2^(b−1) and the factor
  2 cancels the halving:
  a(n) = Σ_m Σ_b (−1)ᵐ·C(m, 4)·(n−m)!·C(n−m, b+1)·C(m−1, b)·2ᵇ,
  with 0 ≤ b < m < n (m = n gives C(0, b+1) = 0). `perm(k)` is k!, and
  `<<b` multiplies the whole product, sign included, by 2ᵇ. One generator
  runs over both indices, so there is no inner `sum`. The program of
  [A001267](../A001267/) is the same with 3 for 4 and the sign flipped.

**Notes**

- Riordan's polynomial recurrence for all the columns at once (the one
  in [A002464](https://oeis.org/A002464)), run on t = B with a base
  B = nⁿ above every coefficient and restarted for each n, is 160 bytes
  for k = 3 and the same here; the column's own recurrence in the entry
  has coefficients of degree 9 and 10 in n.
- Exact integer arithmetic. A count of all permutations agrees for
  n ≤ 9, and the b-file for all its terms.
- Each term costs about n²/2 products, so the whole b-file (201 terms,
  a(0) to a(200)) takes about 4 s here; the bar is all of it in 60 s.
  a(1559) is the first term with more than 4300 digits (Python's
  int-to-str limit), far beyond what the program reaches in practice.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 137 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001268), CC BY-SA 4.0.
