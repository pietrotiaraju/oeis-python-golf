# A000335

> Euler transform of A000292.
> — [OEIS A000335](https://oeis.org/A000335)

Offset 1: 1, 5, 15, 45, 120, 331, 855, 2214, 5545, 13741, 33362, 80091, …

The g.f. is ∏ₖ (1 − xᵏ)^(−w(k)) − 1 with w(k) = C(k + 2, 3) = 1, 4, 10, 20, …,
the tetrahedral numbers ([A000292](https://oeis.org/A000292)): a multiset of
parts in which a part of size k comes in w(k) kinds. (This is the form
MacMahon guessed for 4-dimensional partitions; the true counts,
[A000334](https://oeis.org/A000334), differ from n = 6 on.)

### Python 3 — 96 bytes

```python
R=[1,n:=1]
while[print(R[n])]:n+=1;R+=sum(d*d*~-d*(d-2)*sum(R[d::d])for d in range(-n,0))//6//n,
```

**How it works**

- The log derivative of the product gives
  **n·a(n) = Σ_d d·w(d)·Σ_j a(n − dj)** over d = 1…n and j ≥ 1 with
  dj ≤ n, with a(0) = 1: the [A000219](../A000219/) recurrence with weight
  d·w(d) in place of d².
- `d` runs over −n…−1, so with k = −d the weight is
  6·k·w(k) = k²(k + 1)(k + 2) = d²(d − 1)(d − 2) = `d*d*~-d*(d-2)`
  (`~-d` is d − 1). The four signs cancel, so the sum is 6·n·a(n) and
  `//6//n` is exact.
- `R` is [a(0), …, a(n − 1)], and `R[d::d]` starts |d| places from the end
  and steps back by |d|: a(n − k), a(n − 2k), …, down to a(0).
- The sequence starts at a(1), so the list starts as [a(0), a(1)] = [1, 1]
  with n = 1, and the loop condition prints `R[n]`, the newest term.

**Notes**

- Exact integer arithmetic and exact divisions, so the program is right for
  every n. a(5834) has 778 digits and the digit count grows like n^(4/5),
  so the 4300-digit int-to-str limit is reached only near n = 50 000, far
  beyond what the program gets to.
- About 5800 terms in 60 s here; the bar is the whole b-file (500 terms),
  which prints in under half a second.
- `R=[n:=1]` with `print(R[-1])` would print a(0) = 1 first; starting at
  [1, 1] and printing `R[n]` costs 2 bytes. Counting n downwards as in
  [A000041](../A000041/) (`*R,n=1,1,-1`, `range(n,0)`, `print(R[-1])`) is
  1 byte longer. `~-~-d` for `(d-2)` ties.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 96 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000335), CC BY-SA 4.0.
