# A001245

> Numbers that are the sum of 4 cubes in more than 1 way.
> — [OEIS A001245](https://oeis.org/A001245)

Offset 1: 81, 126, 128, 216, 217, 219, 224, 243, 251, 252, 259, 278, 280, …

The cubes are of non-negative integers (0 is allowed) and a "way" is a
multiset of four cubes: 81 = 0³ + 3³ + 3³ + 3³ = 1³ + 2³ + 2³ + 4³.

### Python 3 — 113 bytes

```python
f=lambda n,k,m:k and sum(f(n-j**3,k-1,j)for j in range(m+1)if j**3<=n)or n<1
n=0
while[f(n,4,n)>1==print(n)]:n+=1
```

**How it works**

- `f(n,k,m)` counts the ways to write n as a sum of k cubes j₁³ + … + j_k³
  with m ≥ j₁ ≥ j₂ ≥ … ≥ j_k ≥ 0. It picks the largest base j ≤ m with
  j³ ≤ n and counts the rest with k − 1 cubes of bases at most j, so every
  multiset is counted exactly once, in non-increasing order.
- The filter `j**3<=n` keeps the remainder non-negative, so at k = 0 the
  remainder is 0 exactly when `n<1`, which is then True (1). With k > 0
  the sum is never 0 for n = 0 (all bases 0 is a way), so `k and … or n<1`
  only falls through to `n<1` when there is no way at all, and n > 0 gives
  False (0).
- The top call uses m = n, which allows every base: j³ ≤ n implies j ≤ n.
- `f(n,4,n)>1==print(n)` is a chained comparison: `print(n)` runs only
  when there are at least two ways. The list around it is always
  non-empty, so `while[…]:n+=1` tests every n ≥ 0 forever.

**Notes**

- The sorted-list method of [A001239](../A001239/) (3 cubes, 152 bytes)
  with a fourth loop is 175 bytes. The recursion is shorter but scans
  n + 1 bases at the top level for each n, so it slows down
  quadratically; that is no problem here, but it would be for A001239's
  bar of 10000 terms.
- Correct for every n; the numbers stay small, so no interpreter limit
  applies.
- The b-file has 1000 terms (up to 6712); the 1000th arrives after about
  17 s here. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 113 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001245), CC BY-SA 4.0.
