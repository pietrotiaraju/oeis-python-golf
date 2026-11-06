# A000391

> Euler transform of A000332.
> — [OEIS A000391](https://oeis.org/A000391)

Offset 1: 1, 6, 21, 71, 216, 672, 1982, 5817, 16582, 46633, 128704, …

The g.f. is ∏ₖ (1 − xᵏ)^(−w(k)) − 1 with w(k) = C(k + 3, 4) = 1, 5, 15, 35, …,
the binomial coefficients of [A000332](https://oeis.org/A000332) from their
first nonzero term on: a multiset of parts in which a part of size k comes
in w(k) kinds. (This is the form MacMahon guessed for 5-dimensional
partitions; the true counts, [A000390](https://oeis.org/A000390), differ
from n = 6 on.) [A000335](../A000335/) is the same with C(k + 2, 3).

### Python 3 — 103 bytes

```python
R=[1,n:=1]
while[print(R[n])]:n+=1;R+=sum(d*d*~-d*(d-2)*(3-d)*sum(R[d::d])for d in range(-n,0))//24//n,
```

**How it works**

- The log derivative of the product gives
  **n·a(n) = Σ_d d·w(d)·Σ_j a(n − dj)** over d = 1…n and j ≥ 1 with
  dj ≤ n, with a(0) = 1: the [A000219](../A000219/) recurrence with weight
  d·w(d) in place of d².
- `d` runs over −n…−1, so with k = −d the weight is
  24·k·w(k) = k²(k + 1)(k + 2)(k + 3) = d²(d − 1)(d − 2)(3 − d) =
  `d*d*~-d*(d-2)*(3-d)` (`~-d` is d − 1; the last factor is written
  3 − d to fix the sign). The sum is 24·n·a(n), so `//24//n` is exact.
- `R` is [a(0), …, a(n − 1)], and `R[d::d]` starts |d| places from the end
  and steps back by |d|: a(n − k), a(n − 2k), …, down to a(0).
- The sequence starts at a(1), so the list starts as [a(0), a(1)] = [1, 1]
  with n = 1, and the loop condition prints `R[n]`, the newest term.

**Notes**

- Exact integer arithmetic and exact divisions, so the program is right for
  every n. a(5500) has 969 digits and the digit count grows like
  n^(5/6), so the 4300-digit int-to-str limit is reached only near
  n = 33 000, far beyond what the program gets to.
- About 5500 terms in 60 s here; the bar is the whole b-file (500 terms),
  which prints in under half a second.
- With t = d² − 3d the product d(d − 1)(d − 2)(d − 3) is t(t + 2), but
  `(t:=d*d-3*d)*~-~t*d` is a byte longer than the plain product. Counting
  n downwards (`*R,n=1,1,-1`, `range(n,0)`, `print(R[-1])`) is 1 byte
  longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 103 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000391), CC BY-SA 4.0.
