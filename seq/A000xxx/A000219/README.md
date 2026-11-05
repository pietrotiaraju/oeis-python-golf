# A000219

> Number of plane partitions (or planar partitions) of n.
> — [OEIS A000219](https://oeis.org/A000219)

Offset 0: 1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500, 859, 1479, 2485, 4167, …

MacMahon's generating function is ∏ₖ (1 − xᵏ)^(−k): a plane partition is a
multiset of parts in which a part of size k comes in k kinds.

### Python 3 — 82 bytes

```python
R=[n:=1]
while[print(R[-1])]:R+=sum(d*d*sum(R[d::d])for d in range(-n,0))//n,;n+=1
```

**How it works**

- The log derivative of ∏ₖ (1 − xᵏ)^(−k) is Σₖ k²·xᵏ/(1 − xᵏ), which gives
  the recurrence on the OEIS page, **n·a(n) = Σ σ₂(k)·a(n − k)** for
  k = 1…n, where σ₂(k) is the sum of the squares of the divisors of k.
  Writing σ₂(k) as Σ d² over d | k and grouping by d turns it into
  **n·a(n) = Σ_d d²·Σ_j a(n − dj)** over d = 1…n and j ≥ 1 with dj ≤ n,
  so no divisors are ever computed.
- `R` is [a(0), …, a(n − 1)], oldest first, and `d` runs over −n…−1. The
  slice `R[d::d]` starts |d| places from the end and steps back by |d|:
  exactly a(n − |d|), a(n − 2|d|), …, stopping when the index would pass
  a(0). `d*d` is the same for d and −d, so the minus signs cost nothing.
- The division by n is exact, so `//` is safe. The new term is appended with
  `R+=…,` and printed by the loop condition on the next pass:
  `while[print(…)]:` is true because `[None]` is a non-empty list.
- `R=[n:=1]` sets a(0) = 1 and the counter n = 1 at once.

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(n) has
  roughly 0.87·n^(2/3) digits (301 at n = 6500), so the 4300-digit int-to-str
  limit is reached only near n = 3.5·10⁵, far beyond what the program gets
  to.
- Term n costs n Python steps plus about n·ln n additions inside the slice
  sums. The whole b-file (6501 terms, n = 0 to 6500) prints in about 27 s
  here and about 9600 terms in a minute; the bar is the whole b-file in
  60 s.
- This is the [A000041](../A000041/) program with `d*d` for `d`. The
  down-counting layout used there (`*a,n=1,0`, `range(n,0)`, `//n`) relies
  on d·Σ being negative when d is; with d² it needs `//-n` and comes to
  83 bytes.
- `for x in R:print(x);` in place of the `while` header is the same length,
  and `sum(d*d*R[d::d])` (repeating the slice d² times) ties
  `d*d*sum(R[d::d])`. Expanding the product directly, by inverting
  ∏ (1 − Xᵏ)ᵏ modulo a power of X = 4ⁿ with `pow(…,-1,M)`, is about
  96 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 82 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000219), CC BY-SA 4.0.
