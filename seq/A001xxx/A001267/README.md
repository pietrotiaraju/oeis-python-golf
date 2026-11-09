# A001267

> One-half the number of permutations of length n with exactly 3 rising or falling successions.
> — [OEIS A001267](https://oeis.org/A001267)

Offset 0: 0, 0, 0, 0, 1, 8, 60, 444, 3599, 32484, 325322, 3582600, 43029621, …

A succession is a position where neighbouring entries differ by 1, as in
1 2 or 4 3. Reversing a permutation keeps its successions and never gives
the same permutation back (n ≥ 2), so the permutations with exactly three
come in pairs and a(n) counts the pairs: column k = 3 of
[A001100](../A001100/), halved.

### Python 3 — 138 bytes

```python
from math import*
n=0
while[print(-sum((-1)**m*comb(m,3)*perm(n-m)*comb(n-m,b+1)*comb(m-1,b)<<b for m in range(n)for b in range(m)))]:n+=1
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
- **Exactly 3.** e(n, m) = Σ_π C(s(π), m), where s(π) is the number of
  successions, so binomial inversion gives the number with exactly j:
  Σ_m (−1)^(m−j)·C(m, j)·e(n, m).
- **The code.** With b − 1 in place of b, 2ᵇ = 2·2^(b−1) and the factor
  2 cancels the halving:
  a(n) = −Σ_m Σ_b (−1)ᵐ·C(m, 3)·(n−m)!·C(n−m, b+1)·C(m−1, b)·2ᵇ,
  with 0 ≤ b < m < n (m = n gives C(0, b+1) = 0). `perm(k)` is k!, and
  `<<b` multiplies the whole product, sign included, by 2ᵇ. One generator
  runs over both indices, so there is no inner `sum`.

**Notes**

- Riordan's polynomial recurrence for all the columns at once (the one
  in [A002464](https://oeis.org/A002464)), run on t = B with a base
  B = nⁿ above every coefficient and restarted for each n, then
  `d//B**3%B//2`, is 160 bytes and 2.5 times slower; the column's own
  recurrence in the entry has coefficients of degree 7 and 8 in n.
- Exact integer arithmetic. A count of all permutations agrees for
  n ≤ 9, and the b-file for all its terms.
- Each term costs about n²/2 products, so the whole b-file (201 terms,
  a(0) to a(200)) takes about 4 s here; the bar is all of it in 60 s.
  a(1559) is the first term with more than 4300 digits (Python's
  int-to-str limit), far beyond what the program reaches in practice.

## First eleven terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(0)…a(10) have to arrive in time.

### Python 3, 11 terms — 124 bytes

```python
from itertools import*
n=0
while[print(sum(sum(-2<x-y<2for x,y in zip(p,p[1:]))==3for p in permutations(range(n)))//2)]:n+=1
```

**How it works**

- The definition, by brute force as on [A001100](../A001100/): for every
  permutation p of 0, …, n−1, count the positions where neighbours differ
  by 1 (`-2<x-y<2`, as the entries are distinct), and count the
  permutations where that number is 3.
- Reversal pairs them off (see above), so the count is even and `//2`
  gives a(n). For n = 0 and 1 the one permutation has no succession.

**Limits**

- Row n costs n! permutations: a(0)…a(9) come within 0.2 s, a(10) after
  about 13 s here (8 reference seconds); a(11) would need about two
  minutes. Exhaustive and exact, so right for every n, only slow.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 138 | first entry |

**Python 3, 11 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 124 | first entry: brute force over all permutations |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001267), CC BY-SA 4.0.
