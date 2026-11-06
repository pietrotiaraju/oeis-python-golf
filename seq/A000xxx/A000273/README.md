# A000273

> Number of unlabeled simple digraphs with n nodes.
> — [OEIS A000273](https://oeis.org/A000273)

Offset 0: 1, 1, 3, 16, 218, 9608, 1540944, 882033440, 1793359192848, …

### Python 3 — 133 bytes

```python
import math
f=lambda r,*L:r<1or sum(f(r+k,*L,k)<<~k+2*sum(map(math.gcd,L,[k]*n))for k in range(-r,0))//r
n=0
while[print(+f(n))]:n+=1
```

**What is counted**

- A simple digraph on n labelled nodes is a subset of the n(n − 1) ordered
  pairs (x, y) with x ≠ y. By Burnside's lemma the number up to relabelling is
  a(n) = (1/n!) Σ_π 2^D(π), where D(π) is the number of orbits of π on those
  ordered pairs.
- If π has cycle lengths l₁, …, l_c, a cycle of length l holds l − 1 orbits
  of pairs inside it (the pairs (x, πᵗx), t = 1, …, l − 1), and two cycles of
  lengths l, m hold gcd(l, m) orbits in each direction (lm pairs, orbits of
  length lcm(l, m)). So D(π) = Σᵢ (lᵢ − 1) + 2 Σ_{i<j} gcd(lᵢ, lⱼ).

**How it works**

- `f(r,*L)` sums over the permutations of r further points, given the lengths
  `L` of the cycles chosen so far. It picks the length k of the cycle through
  one fixed point; that cycle brings 2^(k−1) for the pairs inside it and
  4^gcd(k, l) for each earlier cycle l. So each term is
  `f(…)<<(k-1)+2*Σgcd`.
- Lengths are stored negated: k runs over `range(-r,0)`, the points left are
  `r+k`, `~k` is |k| − 1, and `gcd` ignores the sign.
- `[k]*n` gives `map` a second argument at least as long as `L` (at most n
  cycles).
- `gcd` is used once, so `import math` and `math.gcd` are 1 byte under
  `from math import*` and `gcd`.
- `r<1or` returns `True` when no points are left; the `+` in the print turns
  the `True` of a(0) into 1.

**Dividing by r at every level**

There is no n! anywhere. Choosing the cycle through a fixed point gives
(r − 1)!/(r − k)! permutations for each k, so

g(r, L) = (1/r!) Σ_{σ ∈ S_r} W(L, σ) = (1/r) Σ_k w_k(L) · g(r − k, L + [k]),

and `f` computes the right-hand side with `//r`. That floor is exact because
every g(r, L) is an integer. Fix a permutation τ of a set Y with cycle lengths
L, and let X be the r new points. W(L, σ) is the number of 2-colourings of the
ordered pairs with at least one end in X that σ×τ fixes. By de Bruijn's lemma,
for a group H normal in G and g ∈ G, (1/|H|) Σ_{h∈H} fix(hg) is the number of
H-orbits that g maps to themselves; with H = S_r and g = τ, g(r, L) is such a
count. The same recursion is used in [A000171](../A000171/).

**Notes**

- The recursion visits all 2^(n−1) compositions of n, so the time doubles with
  every term: 24 terms (up to a(23)) in 55 s here. The bar is 20 terms in
  60 s; the b-file has 65 (up to a(64)).
- a(n) ≈ 2^(n(n−1))/n! has about 0.3·n² digits, so Python's 4300-digit
  int-to-str limit would stop the printing at n = 123, far past what the run
  time reaches.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 133 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000273), CC BY-SA 4.0.
