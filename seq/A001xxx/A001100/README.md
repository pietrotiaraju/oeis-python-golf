# A001100

> Triangle read by rows: T(n,k) = number of permutations of length n with exactly k rising or falling successions, for n >= 1, 0 <= k <= n-1.
> — [OEIS A001100](https://oeis.org/A001100)

Offset 1: 1, 0, 2, 0, 4, 2, 2, 10, 10, 2, 14, 40, 48, 16, 2, 90, 230, 256, 120, 22, …

### Python 3 — 139 bytes

```python
from itertools import*
n=1
while[print(sum(sum(-2<x-y<2for x,y in zip(p,p[1:]))==k for p in permutations(range(n))))for k in range(n)]:n+=1
```

**How it works**

- Brute force from the definition: for each row n and each k = 0..n−1,
  count the permutations p of {0, …, n−1} with exactly k positions where
  |p(i+1) − p(i)| = 1.
- The entries of a permutation are distinct, so |x − y| = 1 is the chained
  comparison `-2<x-y<2`, 2 bytes under `abs(x-y)<2`.
- The row is printed by the list comprehension in the `while` header; the
  list holds n `None`s, which is truthy, so the loop goes on to the next
  row.

**Notes**

- Correct for every n by definition; no theorem needed.
- Row n costs n passes over n! permutations: rows 1–9 (45 terms) take
  about 8 s and row 10 about 8 s per term, so about 50 terms come out in
  60 s. The b-file has 10011 terms (rows 1–141); the bar is 40 terms in
  60 s.
- The polynomial recurrence in the entry, S_n(t) = (n+1−t)S_(n−1) − …, is
  provable: inclusion–exclusion gives S_n(t) = Σ_m m!·[x^n] f(x)^m with
  f = x(1+yx)/(1−yx), y = t − 1, and Σ_m m!·u^m satisfies
  u²F′ = F − 1 − uF, which turns into that recurrence for n ≥ 4. A
  program running it on integers t = B (base-B digits) and a two-state
  insertion DP both came out near 170–190 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 139 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001100), CC BY-SA 4.0.
