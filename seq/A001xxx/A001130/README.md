# A001130

> Number of graphical basis partitions of 2n.
> — [OEIS A001130](https://oeis.org/A001130)

Offset 1: 1, 1, 3, 4, 6, 11, 16, 23, 36, 52, 71, 103, 141, 197, 272, 366, 482, 657, 863, 1140, …

A partition is *graphical* if it is the degree sequence of a simple graph.
Write a partition with Durfee square d in Frobenius form: aᵢ = λᵢ − i and
bᵢ = λ′ᵢ − i for i ≤ d (λ′ the conjugate), two strictly decreasing lists of
non-negative integers, weight d + Σaᵢ + Σbᵢ. Its successive ranks are
rᵢ = λᵢ − λ′ᵢ = aᵢ − bᵢ. A *basis partition* (Gupta; Nolan, Savage and Wilf
1998) is one with the fewest cells among all partitions with the same rank
vector (r₁, …, r_d); the basis partitions are counted by
[A066447](https://oeis.org/A066447).

### Python 3 — 203 bytes

```python
from functools import*
r=cache(lambda j,t,D,E:D+j*t<=E and sum(r(j-1,u,max(D+u,0),E-j*abs(u-t))for u in range(t-E//j,t+E//j+1))if j else E|D<1)
n=2
while[print(sum(r(d,1,0,n-d*d)for d in range(n)))]:n+=2
```

**How it works**

- **Basis partitions as rank vectors.** Fix d and r. Since bᵢ = aᵢ − rᵢ,
  the conditions on a are aᵢ − aᵢ₊₁ ≥ max(1, 1 + rᵢ − rᵢ₊₁) and
  a_d ≥ max(0, r_d). All of them are lower bounds on gaps, so the fewest
  cells come from taking every one with equality, and that partition is the
  only minimum. Summing the gaps, its weight is
  d² + Σⱼ₌₁..d j·|rⱼ − rⱼ₊₁| with r_d₊₁ = 0. So a basis partition is just a
  d ≥ 1 and any integer vector r, and with hᵢ = rᵢ + 1 (h_d₊₁ = 1) the
  weight is d² + Σ j·|hⱼ − hⱼ₊₁|. (This gives A066447's generating function
  Σ q^(d²) ∏ⱼ≤d (1 + qʲ)/(1 − qʲ) as a check.)
- **Graphical.** By Erdős–Gallai, a partition of an even number is graphical
  iff Σᵢ≤ₖ λᵢ ≤ Σᵢ≤ₖ (λ′ᵢ − 1) for k = 1, …, d: for k ≤ d the right side
  is exactly k(k − 1) + Σᵢ>ₖ min(λᵢ, k), and the inequalities past the
  Durfee size follow from these (the conjugate form of the criterion, see
  Sierksma and Hoogeveen, *Seven criteria for integer sequences being
  graphic*, 1991). That reads Σᵢ≤ₖ hᵢ ≤ 0 for every k ≤ d: the condition
  depends only on the rank vector.
- **Counting.** `r(j,t,D,E)` fills the positions j, j − 1, …, 1 in reverse:
  `t` is h at position j + 1, `E` the weight left above the j² that the
  positions j..1 need anyway, so choosing hⱼ = `u` costs j·|u − t|. The
  prefix conditions are carried backwards as a Lindley recursion: the prefix
  sum before position j must be at most −D, so `D` becomes `max(D+u,0)`,
  and at the start (j = 0, empty prefix) both `D` and `E` must be 0
  (`E|D<1`; both are non-negative there). Each term is
  Σ_d `r(d,1,0,2n-d*d)`; for d² > 2n the range is empty.
- **Pruning.** The remaining positions sum to j·t − Σ l·(h_l₊₁ − h_l) ≥
  j·t − E, and that sum must be at most −D, so a state with D + j·t > E
  counts nothing. Without this test the program is about twice as slow. The memo is shared by all terms, since `E` is the weight still
  to place.

**Notes**

- Exact integer counting; correctness rests only on the two facts above
  (the basis characterization and the Erdős–Gallai criterion). A brute force
  over all partitions of 2n with the full Erdős–Gallai test agrees for
  n ≤ 16, and the program matches all 100 b-file terms.
- The b-file (from Nolan, Sivaraman, Savage and Tiwari, *Graphical basis
  partitions*, Graphs Combin. 14 (1998)) has 100 terms; the program prints
  them all in about 30 s here, with about 1.6 million memo entries
  (250 MB). The bar is the whole b-file in 80 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 203 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001130), CC BY-SA 4.0.
