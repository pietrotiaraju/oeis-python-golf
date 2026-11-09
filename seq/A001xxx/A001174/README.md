# A001174

> Number of oriented graphs (i.e., digraphs with no bidirected edges) on n unlabeled nodes. Also number of complete digraphs on n unlabeled nodes. Number of antisymmetric relations (i.e., oriented graphs with loops) on n unlabeled nodes is A083670.
> — [OEIS A001174](https://oeis.org/A001174)

Offset 1: 1, 2, 7, 42, 582, 21480, 2142288, 575016219, 415939243032, 816007449011040, 4374406209970747314, …

### Python 3 — 138 bytes

```python
import math
f=lambda r,*L:r<1or sum(f(r+k,*L,k)*3**(~k//2+sum(map(math.gcd,L,[k]*n)))for k in range(-r,0))//r
n=1
while[print(+f(n))]:n+=1
```

Same recursion as the digraph program of
[A000273](../../A000xxx/A000273/), with three states per pair instead of
two per ordered pair.

**What is counted**

- An oriented graph gives each unordered pair {x, y} of distinct nodes one of
  three states: no edge, x → y, or y → x. By Burnside's lemma the number up to
  relabelling is (1/n!) Σ_π W(π), with W(π) the number of oriented graphs that
  π fixes.
- π permutes the unordered pairs. A fixed oriented graph is constant on each
  orbit, and an orbit gives a factor 3, except an orbit in which some power of
  π swaps the two ends of a pair: there a fixed graph cannot orient the pair,
  so the factor is 1.
- Two cycles of lengths l, m hold gcd(l, m) orbits of pairs between them, and
  no power of π swaps ends there (they lie in different cycles): factor
  3^gcd(l, m). A cycle of length l holds ⌊l/2⌋ orbits of pairs inside it; for
  even l one of them is the pairs {x, π^(l/2)x}, whose ends π^(l/2) swaps. So
  the factor inside is 3^⌊(l−1)/2⌋, and
  W(π) = 3^(Σᵢ ⌊(lᵢ−1)/2⌋ + Σ_{i<j} gcd(lᵢ, lⱼ)).

**How it works**

- `f(r,*L)` sums over the permutations of r further points, given the cycle
  lengths `L` chosen so far: it picks the length k of the cycle through one
  fixed point and multiplies by 3^(⌊(k−1)/2⌋ + Σ_{l∈L} gcd(k, l)).
- Lengths are stored negated (k in `range(-r,0)`), so `~k` is |k| − 1 and
  `~k//2` is ⌊(|k|−1)/2⌋; `gcd` ignores the sign.
- `//r` at every level is exact for the reason given on
  [A000273](../../A000xxx/A000273/): by de Bruijn's form of Burnside's lemma
  each partial sum counts orbits of S_r (on oriented graphs of the pairs with at
  least one new end) that a fixed permutation of the other points maps to
  themselves.
- `r<1or` returns `True` when no points are left; `+` prints a(1) as 1.

**Notes**

- Exact for every n.
- The recursion visits all 2^(n−1) compositions of n, so the time doubles with
  every term: 21 terms in 15 s on the PC it was written on. The b-file has 50;
  the bar is 21 terms in 60 s.
- Caching `f` on sorted `L` (`functools.cache`, 176 bytes) reaches about 40
  terms in the same time.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 138 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001174), CC BY-SA 4.0.
