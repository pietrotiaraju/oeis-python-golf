# A000055

> Number of trees with n unlabeled nodes.
> — [OEIS A000055](https://oeis.org/A000055)

Offset 0: 1, 1, 1, 1, 2, 3, 6, 11, 23, 47, 106, 235, 551, 1301, 3159, 7741, …

### Python 3 — 137 bytes

```python
F=1,;n=-1
while[print(F[n]+sum(F[i]*((i-~i==n)-F[n+~i])for i in range(n))//2)]:n+=1;F+=sum(d*F[~d]*sum(F[d::d])for d in range(~n,0))//~n,
```

**How it works**

- Otter's formula from the OEIS page: A(x) = 1 + T(x) − (T(x)² − T(x²))/2,
  where T(x) = x + x² + 2x³ + 4x⁴ + … counts rooted trees
  ([A000081](https://oeis.org/A000081)). Taking the x^m coefficient,
  **a(m) = r(m) − (Σ r(i)·r(m−i) − r(m/2))/2**, summed over 0 < i < m,
  with the r(m/2) term only for even m. The bracket counts sets of two
  distinct rooted trees with m nodes in total.
- `F` holds rooted forests: F(k) = r(k+1) is the number of forests with k
  nodes, since removing a root leaves a forest. In these terms the loop
  prints a(n+1) = F(n) + Σ F(i)·([2i+1 = n] − F(n−1−i))/2 over i < n.
  `i-~i` is 2i+1 and `n+~i` is n−1−i.
- Forests satisfy the Euler-transform recurrence
  **k·F(k) = Σ_d d·F(d−1)·Σ_{j≥1} F(k−jd)**, summed over 1 ≤ d ≤ k
  (the A000081 recurrence with its two sums swapped). After `n+=1` the tuple
  holds F(0) … F(n), so with d running over −(n+1) … −1, `F[~d]` is
  F(|d|−1), the slice `F[d::d]` walks back from F(n+1−|d|) in steps of |d|,
  and dividing the negative sum by `~n` = −(n+1) gives F(n+1).
- `n=-1` prints a(0) first: `F[-1]` is F(0) = 1 and the sum over `range(-1)`
  is empty. Python's negative indexing does the special case for free.
- `F+=…,` concatenates a one-item tuple; `while[print(…)]` prints and loops forever
  because `[None]` is a non-empty list.

**Notes**

- Exact integer arithmetic, so the program is right for every n: both
  divisions are exact (the recurrence's sum is a multiple of k, and
  r(i)·r(m−i) pairs up apart from the middle term r(m/2)² − r(m/2), which is
  even).
- Each term costs O(n log n) big-integer operations, so the whole b-file
  (1001 terms, n up to 1000) prints in under a second and about 3700 terms
  print in 60 s. The bar is the whole b-file in 60 s.
- a(n) ~ 0.5349 · 2.9558ⁿ · n^(−5/2) (Otter), so from about n = 9160 its
  decimal form passes Python's 4300-digit int-to-str limit.
- The same length (138) comes from listing r itself with a sentinel
  r(0) = −2: the i = 0 term of the sum then supplies the 2·r(m), so
  a(m) = Σ r(i)·([2i = m] − r(m−i))/2 over i < m, at the cost of `or 1`
  for a(0) and a `:0` stop in the slices so the sentinel stays out of the
  recurrence.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 138 | first entry |
| 2026-11-06 | Python 3 | 137 | use a tuple for the initial F state |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000055), CC BY-SA 4.0.
