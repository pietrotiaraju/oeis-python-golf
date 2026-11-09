# A000637

> Number of fixed-point-free permutation groups of degree n.
> — [OEIS A000637](https://oeis.org/A000637)

Offset 0: 1, 0, 1, 2, 7, 8, 37, 40, 200, 258, 1039, 1501, 7629, 10109, …

Groups are counted up to conjugacy in S_n, as in [A000638](../A000638/).

### Python 3 — 292 bytes

```python
from itertools import*
n=0;D=[];q=1
while S:=[*permutations(range(n))]:
 for K in(L:=[{S[0]}]):
  for g in S:
   J=K|{g}
   while J<(J:={tuple(a[i]for i in b)for a in J for b in J}):0
   if J not in D:D+=[{tuple(s.index(p[x])for x in s)for p in J}for s in S];L+=J,
 print(-q+(q:=len(L)));n+=1
```

**How it works**

- a(n) = [A000638](../A000638/)(n) − A000638(n − 1) (Christian G. Bower's
  formula on the OEIS page). The subgroups of S_n with a fixed point are,
  up to conjugacy, the subgroups of S_{n−1} fixing the last point, and two
  of them conjugate in S_n are already conjugate in S_{n−1}: if σHσ⁻¹ = H′,
  then H fixes both n − 1 and f = σ⁻¹(n − 1), so the transposition
  (f, n − 1) commutes with H, and σ∘(f, n − 1) fixes the last point and
  still conjugates H to H′.
- The search is the [A000638](../A000638/) record: closures of K ∪ {g} over
  class representatives K and all g ∈ S_n, with a list `D` of all
  conjugates of the classes found; `len(L)` is A000638(n) + 1.
- `q` keeps the previous `len(L)`, so `-q+(q:=len(L))` prints the
  difference and stores the new value. It starts at 1, the value for
  A000638(−1) = 0, which gives a(0) = 1 (the group of degree 0 fixes
  nothing) and a(1) = 0, as in the OEIS data.

**Notes**

- Exhaustive search, right for every n, only slow: a(0) … a(4) print in a
  second, a(5) takes about 45 s on this PC, and a(6) is out of reach. The bar
  is 6 terms in 120 s.

## First four terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(0)…a(3) have to arrive in time.

### Python 3, 4 terms — 251 bytes

```python
from itertools import*
n=q=0
while P:=[*permutations(range(n))]:print(-q+(q:=sum({tuple(a[i]for i in b)for a in H for b in H}=={*H}=={tuple(g.index(h[x])for x in g)for h in H}for k in range(len(P))for H in combinations(P,k+1)for g in P)//len(P)));n+=1
```

**How it works**

- a(n) = A000638(n) − A000638(n − 1), as in the main record: up to
  conjugacy, the groups of degree n with a fixed point are the groups of
  degree n − 1.
- The sum is the [A000638](../A000638/) short record, whose page has the
  argument: Burnside's lemma for S_n acting on its subgroups by conjugation.
  It counts the pairs (H, g) of a nonempty subset H of S_n and a g ∈ S_n
  such that the products a∘b of H are exactly H (so H is a subgroup) and
  g⁻¹Hg = H, and divides by n!: the number of conjugacy classes of
  subgroups.
- `q` keeps the previous count, so `-q+(q:=…)` prints the difference and
  stores the new value. It starts at 0, the value of A000638(−1), which gives
  a(0) = 1 (the group of degree 0 fixes nothing) and a(1) = 0.

**Limits**

- a(3) takes 63 subsets of S_3 times 6 conjugations.
  The four terms arrive in a fraction of a second.
- a(4) would test 2²⁴ − 1 ≈ 1.7·10⁷ subsets of S_4 against 24 conjugations
  each, every test squaring the subset: many hours. The main record builds
  subgroups by closure, one class at a time, and reaches six terms.
- Everything is exact and exhaustive, so the program is right for every n;
  it is only slow.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-07 | 292 | first entry |

**Python 3, 4 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 251 | first entry: Burnside over all subsets of S_n and all conjugations, difference of degrees |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000637), CC BY-SA 4.0.
