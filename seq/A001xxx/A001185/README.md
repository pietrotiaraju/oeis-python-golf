# A001185

> Number of nontrivial Baxter permutations of length 2n-1.
> — [OEIS A001185](https://oeis.org/A001185)

Offset 1: 0, 1, 1, 7, 21, 112, 456, 2603, 13203, …

### Python 3 — 181 bytes

```python
f=lambda p,u,i=0:sum(f([v]+p,u-{v},i+1)for v in u-{i}if min((p[0]-x)*(v-x)for x in[p,u][i%2])>=v-i&1)if u else([p[p[k]]for k in p]==p)+1
n=3
while[print(f([n],{*range(n)})//4)]:n+=2
```

**How it works**

- Same title as [A001183](../A001183/), which counts the nontrivial
  (fixed-point free) Baxter permutations of order N = 2n+1 in W. M. Boyce's
  sense (definition and indexing on that page). This sequence is the next
  column of Boyce's 1967 table, "Eq. cl. of NT": the number of classes
  {P, P⁻¹, UPU, UP⁻¹U} of nontrivial ones, with U(i) = N+1−i. Swapping f
  and g turns P into P⁻¹, and conjugating both by x ↦ 1−x turns it into
  UPU; neither changes whether f and g share a fixed point.
- The classes are the orbits of the Klein group {e, σ, τ, στ}, σP = P⁻¹,
  τP = UPU, on the nontrivial set X, so by Burnside their number is
  (|X| + |Fix σ| + |Fix τ| + |Fix στ|)/4. Two of the terms vanish:
  UPU = P gives P(c) = c at the middle c = (N+1)/2, a fixed point; and P⁻¹ = P
  is impossible too, because P keeps parity, one of the sets of odd values
  ((N+1)/2 of them) and of even values ((N−1)/2) has odd size, and an
  involution of an odd-size set has a fixed point. So the count is
  (|X| + #{P ∈ X : P = UP⁻¹U})/4, and P = UP⁻¹U says exactly that PU is an
  involution.
- The search is A001183's (values and positions from 0, U(i) = N−1−i):
  it builds `p` newest first after the sentinel N, so a finished `p` reads
  P(N−1), …, P(0), N, which is PU followed by N ↦ N, a permutation of
  0 … N. `[p[p[k]]for k in p]==p` says p∘p∘p = p, that is p∘p = identity.
  Each leaf adds 1, or 2 when PU is an involution, and the total is divided
  by 4.
- Away from the leaves `if u` takes the sum; `p[p[k]]` would fail on a
  partial list, which is why the leaf is not counted with `i//n` as in
  A001183.

**Notes**

- Exact integers. Before golfing, the classes were also counted directly
  (one smallest member per class {P, P⁻¹, UPU, UP⁻¹U}) for all 9 terms,
  with the same result.
- All 9 terms take about 5 s here; the next one, a(10) = 77748 (beyond the
  OEIS data), comes after about 40 s.
- `-~(…)` would be as short as `(…)+1`, but `~` on a bool warns in 3.12.
- The b-file is the OEIS entry's 9 terms; the bar is all of them in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 181 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001185), CC BY-SA 4.0.
