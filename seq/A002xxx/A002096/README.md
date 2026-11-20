# A002096

> Mixed partitions of n.
> — [OEIS A002096](https://oeis.org/A002096)

Offset 1: 0, 0, 1, 2, 3, 6, 9, 14, 20, 29, 42, 58, 79, 108, 145, 191, …

### Python 3 — 103 bytes

```python
f=lambda n,j=1,s=0,F=1:s-n>2if j>n else f(n-j,j,s|F%j+1,F)+f(n,j+1,s,F*j*j)
n=1
while[print(f(n))]:n+=1
```

**How it works**

- **Definition.** The entry's comment: partitions of n with at least one
  prime part and at least one nonprime part (1 counts as nonprime). It
  agrees with the entry's formula a(n) = Σ_{k=1..n−1} A000607(n − k)·A002095(k):
  the partition generating function factors as (primes only)·(nonprimes
  only), and dropping the k = 0 and k = n terms removes the partitions of a
  single kind. It reproduces all 46 terms of the b-file.
- `f(n,j,s,F)` counts the ways to finish a partition of the remainder n
  with parts ≥ j, taken in increasing order: either use one more part j
  (and stay at j), or move on to j + 1. Every partition is reached exactly
  once.
- `s` is a 2-bit mask of the kinds used so far: `F%j+1` is 2 for a prime
  part and 1 for a nonprime part, because F = ((j − 1)!)² and, by Wilson's
  theorem, F mod j is 1 exactly when j is prime (0 for j = 1, and for j = 4,
  where F = 36). `F*j*j` moves F along with j.
- When j > n nothing more fits, so the branch is a finished partition only
  if n = 0, and it counts only if both bits are set: `s-n>2` (with s ≤ 3 and
  n ≥ 0) is exactly n = 0 and s = 3. Every other call returns a sum of two
  such booleans, an integer.

**Notes**

- A plain search: it walks every partition of n, so the time grows like
  p(n). The b-file has 46 terms (n = 1 to 46), the bar, and they take about
  2 s here.
- The recursion is about 2n calls deep (n part steps and n part-size steps
  at most), so Python's default recursion limit would stop it near n = 500,
  long after the time limit.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 103 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002096), CC BY-SA 4.0.
