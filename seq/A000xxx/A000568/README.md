# A000568

> Number of outcomes of unlabeled n-team round-robin tournaments.
> — [OEIS A000568](https://oeis.org/A000568)

Offset 0: 1, 1, 1, 2, 4, 12, 56, 456, 6880, 191536, …

a(n) is the number of tournaments on n unlabelled vertices.

### Python 3 — 171 bytes

```python
import math,functools as F
f=F.cache(lambda r,*L:r<1or sum(f(r-k,*sorted(L+(k,)))<<k//2+sum(map(math.gcd,L,[k]*n))for k in range(1,r+1,2))//r)
n=0
while[print(+f(n))]:n+=1
```

**What is counted**

- By Burnside's lemma a(n) = (1/n!) Σ_π fix(π), where fix(π) is the number
  of labelled tournaments that the vertex permutation π maps to themselves.
- If π has a cycle of even length k, then π^(k/2) swaps the two ends of the
  pair {x, π^(k/2)x} inside it and reverses that arc, so fix(π) = 0. If all
  cycles are odd, no orbit of π on the unordered pairs contains a pair
  together with its reverse, so each orbit can be oriented in 2 ways and
  fix(π) = 2^(number of orbits). A cycle of odd length k has (k − 1)/2
  orbits on its own pairs, and two cycles of lengths k and l have gcd(k, l)
  orbits of pairs between them. Grouped by cycle type this is Davis's
  formula (1954), the formula line on the entry.

**How it works**

- `f(r,*L)` is (1/r!) Σ_σ 2^N(σ) over the permutations σ of r further
  points with odd cycles only, given the lengths `L` of the cycles already
  chosen, where N counts the orbits of pairs that touch one of the r points.
  The cycle through one fixed point has length k in (r − 1)!/(r − k)! ways,
  so

  f(r, L) = (1/r) Σ_{k odd ≤ r} 2^((k−1)/2 + Σ_{l∈L} gcd(k, l)) · f(r − k, L + [k]),

  the [A000171](../A000171/) recursion with tournament weights; f(n) with
  no cycles yet is a(n).
- `range(1,r+1,2)` leaves out the even cycles, whose weight is 0, and
  `k//2` is (k − 1)/2 for odd k. The exponent sits right of `<<` with no
  parentheses since `<<` binds looser than `+`.
- `map(math.gcd,L,[k]*n)` pairs k with every earlier cycle: `L` has at most
  n entries. `r<1or` returns `True` when no points are left; the `+` in the
  print turns the `True` of a(0) into 1.
- **The cache.** f(r, L) only depends on the multiset L, so the call passes
  `*sorted(L+(k,))` and `functools.cache` merges all orders of the same
  cycles: the states are pairs (r, partition of n − r into odd parts)
  instead of compositions. The value does not depend on n (`[k]*n` is only a
  length), so the cache stays valid from one n to the next.

**Dividing by r at every level**

The `//r` is exact because every f(r, L) is an integer, the same argument as
for [A000171](../A000171/). Fix a permutation τ of a set Y with cycle lengths
L. Then 2^N(σ) is the number of orientations of the pairs that touch the r
points X that σ×τ fixes (zero if σ has an even cycle). By de Bruijn's lemma,
for a group H normal in G and g ∈ G, (1/|H|) Σ_{h∈H} fix(hg) is the number of
H-orbits that g maps to themselves; with H = S_r and g = τ, f(r, L) is such a
count. So the program never needs n! or the class sizes of the cycle types.

**Notes**

- Other versions that print the same terms: the same recursion without the
  cache, `f=lambda r,*L:…f(r-k,*L,k)…` with `import math`: 136 bytes, but
  the composition tree grows like the Fibonacci numbers and it prints only
  32 terms in 60 s, below the bar; Davis's partition sum scaled by n!: 291
  bytes.
- Exact integer arithmetic; correctness for every n rests only on Burnside's
  lemma and the orbit count above.
- About 70 terms in 60 s here, with the cache at about 0.55 GB by then. The
  b-file has 77 terms (up to a(76)); the bar is 35 terms in 60 s.
- a(n) is close to 2^C(n,2)/n!, which first has more than 4300 digits near
  n = 176, so the int-to-str limit is far beyond a 60-s run.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 308 | first entry |
| 2026-11-06 | Python 3 | 291 | cached partition expression and occurrence-index class factors |
| 2026-11-07 | Python 3 | 171 | A000171-style cycle recursion, `//r` at every level, cached on the sorted cycle list |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000568), CC BY-SA 4.0.
