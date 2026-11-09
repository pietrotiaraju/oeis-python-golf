# A000595

> Number of binary relations on n unlabeled points.
> — [OEIS A000595](https://oeis.org/A000595)

Offset 0: 1, 2, 10, 104, 3044, 291968, 96928992, 112282908928, 458297100061728, 6666621572153927936, …

### Python 3 — 171 bytes

```python
import math,functools
f=functools.cache(lambda r,*L:r<1or sum(f(r-k,*sorted((*L,k)))<<k+2*sum(map(math.gcd,L,[k]*n))for k in range(1,r+1))//r)
n=0
while[print(+f(n))]:n+=1
```

**How it works**

- **Burnside's lemma.** A binary relation is a set of ordered pairs (x, y),
  x = y allowed, so a(n) = (1/n!) Σ_σ 2^T(σ), where T(σ) is the number of
  orbits of the permutation σ on the n² ordered pairs. Two cycles of
  lengths i and j have gcd(i, j) orbits on the pairs from the first to the
  second and gcd(i, j) on the pairs back; one k-cycle has k orbits on its own
  k² pairs.
- **The recursion.** As in [A000250](../A000250/), `f(r,*L)` is
  (1/r!) Σ_σ 2^N(σ) over the permutations σ of r further points, given the
  lengths L of the cycles already chosen, where N counts only the orbits of
  pairs that touch one of the r points. The cycle through one fixed point
  has length k in (r − 1)!/(r − k)! ways, so

  f(r, L) = (1/r) Σ_{k=1}^{r} 2^(k + 2·Σ_{l∈L} gcd(k, l)) · f(r − k, L + [k]),

  and f(n) with no cycles yet is a(n). In the code the power is a shift,
  `<<k+2*sum(map(math.gcd,L,[k]*n))` (`[k]*n` is long enough, since L has at
  most n entries), and `r<1or` returns `True` when no points are left, which
  counts as 1.
- **Exact `//r`.** f(r, L) is an integer: by de Bruijn's form of Burnside's
  lemma, (1/|H|) Σ_{h∈H} fix(hg) is the number of H-orbits that g maps to
  themselves, for H = S_r on the new points and g a fixed permutation of
  cycle type L on the others. So the sum over k is r times an integer.
- **The cache.** f depends only on r and the multiset L, so the cycle
  lengths are passed sorted and `functools.cache` evaluates each pair
  (r, partition of n − r) once: about 450 000 states for n = 44, against
  2^43 compositions without the cache.
- `+f(n)` turns the `True` that f(0) returns into 1 for a(0).

**Notes**

- Other versions that print the same terms:
  - the same recursion without the cache, `*L,k` unsorted: 133 bytes, but it
    visits every composition and prints only 23 terms in 60 s here, under
    the bar;
  - a partition recursion that carries the class size n!/z as an argument,
    `f=lambda r,m,w,*L:r<1and w or sum(f(r-k,k,w//k//-~L.count(k),*L,k)<<…`
    with `while[print(f(n,1,H)//H)]:n+=1;H*=n`: 176 bytes, the whole b-file in
    about 60 s with almost no memory;
  - the first version of this page, a cached partition list with explicit
    class sizes: 294 bytes.
- Exact integer arithmetic, so the program is right for every n.
- About 44 terms in 60 s here. The cache keeps the states of every n seen so
  far: about 480 MB after 60 s. The b-file has 51 terms (up to a(50)); the bar
  is 25 terms in 60 s.
- a(n) ~ 2^(n²)/n! (McIlroy 1955), so a(123), with about 4350 digits, is the
  first term past the 4300-digit int-to-str limit, far beyond reach.

## First 23 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(0)…a(22) have to arrive in time.

### Python 3, 23 terms — 133 bytes

```python
import math
f=lambda r,*L:r<1or sum(f(r-k,*L,k)<<k+2*sum(map(math.gcd,L,[k]*n))for k in range(1,r+1))//r
n=0
while[print(+f(n))]:n+=1
```

**How it works**

- The same recursion as the main record,

  f(r, L) = (1/r) Σ_{k=1}^{r} 2^(k + 2·Σ_{l∈L} gcd(k, l)) · f(r − k, L + [k]),

  with the same Burnside argument for every n. Only the cache is gone.
  Without `functools.cache` the cycle lengths need no sorting, so
  `f(r-k,*L,k)` appends k as it comes, and `functools` is not imported.
- The value of f depends only on the multiset of cycle lengths, since the
  gcd sum ignores their order. So each call returns the same integer as in
  the cached version, and `//r` stays exact.

**Limits**

- Without the cache f walks every composition of n, 2^(n−1) of them for
  a(n), so each term takes about twice as long as the one before. Here
  a(22) arrives after about 24 s (about 12 reference seconds), a(23) after
  48 s, and a(24), the 25th term of the main bar, is out of reach.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-06 | 294 | first entry |
| 2026-11-07 | 171 | A000250-style recursion with exact `//r`, cached on sorted cycle lengths |

**Python 3, 23 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 133 | first entry: the main recursion without the cache |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000595), CC BY-SA 4.0.
