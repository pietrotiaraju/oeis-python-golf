# A000171

> Number of self-complementary graphs with n nodes.
> — [OEIS A000171](https://oeis.org/A000171)

Offset 1: 1, 0, 0, 1, 2, 0, 0, 10, 36, 0, 0, 720, 5600, 0, 0, 703760, 11220000, …

### Python 3 — 147 bytes

```python
from math import*
f=lambda r,*L:r<1or sum(n%4%3*f(r+k,*L,k)<<2*~k+4*sum(map(gcd,L,[k]*n))for k in range(-r,0))//r
n=2
while[print(+f(n+1>>2))]:n+=1
```

**What is counted**

- A graph on n labelled vertices is self-complementary when some permutation
  π of the vertices maps it onto its complement. Burnside's lemma on the coset
  "π, then complement" gives a(n) = (1/n!) Σ_π fix(π̄), where π̄ sends G to the
  complement of π(G).
- π̄ fixes G exactly when G alternates in and out along every edge cycle of π,
  so fix(π̄) = 2^(number of edge cycles) if all edge cycles have even length,
  and 0 otherwise. That happens exactly when every vertex cycle of π has length
  divisible by 4, apart from at most one fixed point (Read, 1963). So
  a(n) = 0 for n ≡ 2, 3 (mod 4).
- Write those cycles as 4v₁, …, 4v_c, with v a partition of m = ⌊n/4⌋. The
  edge cycles are 2v inside a 4v-cycle, 4·gcd(v, w) between two cycles, and one
  between the fixed point (n odd) and each cycle. Putting in the number of
  such π and cancelling the powers of 2 gives

  a(n) = (1/m!) Σ_{σ ∈ S_m} e^c(σ) · 4^D(σ),

  where c(σ) is the number of cycles of σ, D(σ) the number of its orbits on
  ordered pairs (x, y) with x ≠ y, and e = 1 for n ≡ 0, e = 2 for n ≡ 1 (mod 4).
- Read through Burnside again, this is the number of ways, up to relabelling
  the m points, to give each ordered pair of distinct points one of 4 colours
  and each point one of e colours.

**How it works**

- `f(r,*L)` sums over the permutations of r further points, given the lengths
  `L` of the cycles chosen so far. It picks the length k of the cycle through
  one fixed point; that cycle brings e·4^(k−1) (its point orbit and k − 1
  orbits of pairs inside it) and 16^gcd(k, l) for each earlier cycle l
  (gcd(k, l) orbits in each direction). So each term is
  `e*f(…)<<2*(k-1)+4*Σgcd`.
- Lengths are stored negated: k runs over `range(-r,0)`, the points left are
  `r+k`, `2*~k` is 2(|k| − 1), and `gcd` ignores the sign. This saves the
  `-~` that `range(r)` would need twice.
- `[k]*n` is only there to give `map` a second argument at least as long as
  `L` (which has at most m ≤ n entries).
- The loop variable `n` is the index plus 1: `n%4%3` is e = 1, 2, 0, 0 for
  indices ≡ 0, 1, 2, 3 (mod 4) and `n+1>>2` is m. For indices ≡ 2, 3 every
  cycle brings the factor 0, and m ≥ 1 there, so the zeros need no special
  case.
- `r<1or` returns `True` for no points left; the `+` in the print turns the
  `True` of a(1) into 1.

**Dividing by r at every level**

The program never computes m!. Choosing the cycle through a fixed point gives
the usual count (r − 1)!/(r − k)! for each k, so

g(r, L) = (1/r!) Σ_{σ ∈ S_r} W(L, σ) = (1/r) Σ_k w_k(L) · g(r − k, L + [k]),

and `f` computes the right-hand side with `//r`. That floor is exact because
every g(r, L) is an integer. Fix a permutation τ of a set Y with cycle lengths
L. W(L, σ) is the number of colourings of X×X, X×Y and Y×X (X the r points,
the same colours as above) fixed by σ×τ. By de Bruijn's lemma, for a group H
normal in G and g ∈ G, (1/|H|) Σ_{h∈H} fix(hg) is the number of H-orbits that
g maps to themselves. With H = S_r and g = τ, g(r, L) is such a count. This is
the same lemma as in the first step, where H = S_n and g = complement.

**Notes**

- The recursion visits all 2^(m−1) compositions of m, so the time doubles every
  4 terms: about 85 terms in 60 s here. The bar is 65 terms in 60 s; the b-file
  has 100.
- a(n) has about 0.034·n² digits, so Python's 4300-digit int-to-str limit
  stops the printing near n = 356, long after the run time does.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 147 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000171), CC BY-SA 4.0.
