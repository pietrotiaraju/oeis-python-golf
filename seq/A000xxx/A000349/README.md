# A000349

> One-half the number of permutations of length n with exactly 2 rising or falling successions.
> — [OEIS A000349](https://oeis.org/A000349)

Offset 0: 0, 0, 0, 1, 5, 24, 128, 835, 6423, 56410, 554306, …

### Python 3 — 129 bytes

```python
from math import*
n=0
while[R:=range(n),print(sum((-1)**m*m*~-m*(n-m)*comb(n-m,j)*perm(n+~j,n+~m)for m in R for j in R)//4)]:n+=1
```

**How it works**

- A rising or falling succession is an adjacent pair of values i, i+1 in
  either order. Mark any m of the successions of a permutation of [n]:
  the marked pairs glue the values into k = n − m blocks of consecutive
  integers, each block of length ≥ 2 laid out increasing or decreasing,
  and the blocks can come in any of k! orders. So the number of
  (permutation, marked set) pairs is N_m = k!·c(k, m), where c(k, m)
  counts compositions of n into k parts with weight 2 for each part of
  length ≥ 2: `c(k, m) = [yᵐ]((1+y)/(1−y))ᵏ`, since a part of length ℓ
  contributes 2y^(ℓ−1) (or 1 for ℓ = 1). Expanding (1+y)ᵏ(1−y)⁻ᵏ gives
  c(k, m) = Σⱼ C(k, j)·C(m−j+k−1, k−1).
- Summing t^(successions) over permutations is Σ_m N_m·(t−1)^m (each
  marked set counts once), so the number with exactly two successions is
  Σ_m (−1)^m·C(m, 2)·N_m, and a(n) is half of it:
  a(n) = Σ_{m,j} (−1)^m·m(m−1)·(n−m)!·C(n−m, j)·C(n−j−1, n−m−1)/4.
- (n−m)!·C(n−j−1, n−m−1) is (n−m)·perm(n−j−1, n−m−1), which saves a
  `perm`. `n+~j` and `n+~m` are n−1−j and n−1−m.
- Both indices run over `R`, range(n), named in the loop header (a
  walrus cannot be the iterable of a comprehension). m < n leaves out
  k = 0, and the terms with j > k or j > m vanish by themselves: `comb`
  and `perm` return 0 when the lower index is larger, and no argument is
  ever negative. At n = 0 the sum is empty.

**Notes**

- Exact integer arithmetic, correct for every n: the formula is the
  inclusion–exclusion above (the same count as Robbins' and Lang's
  formula in [A001100](https://oeis.org/A001100)). Each term is a double
  sum of n² products, so the run time grows like n³: on the machine that
  set the bar the whole b-file (201 terms, n = 0 to 200) prints in about
  7 s, and about 340 terms in 60 s. The bar is the whole b-file in 60 s.
- With c(k, m) = Σⱼ 2ʲ·C(k, j)·C(m−1, j−1) instead it is 136 bytes. The
  four-term recurrence for the polynomials S_n(t) of
  [A002464](https://oeis.org/A002464), evaluated at t = nⁿ and read off
  in base nⁿ, has to be rerun for every n and is over 170 bytes, and an
  insertion DP on (successions, is n−1 next to n) needs two lists with
  index weights.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 129 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000349), CC BY-SA 4.0.
