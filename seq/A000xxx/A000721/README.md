# A000721

> Number of NP-equivalence classes of balanced Boolean functions of n variables.
> — [OEIS A000721](https://oeis.org/A000721)

Offset 1: 1, 2, 6, 74, 169112, 39785643746726, 37126652766640082937217814348006, …

### Python 3 — 263 bytes

```python
from itertools import*
n=1
while 1:
 t=c=0;X=2**2**n
 for*m,p in product(range(2**n),permutations(range(n))):
  for w in p:m+=[y^1<<w for y in m];P=1
  for x in m:
   Q=1
   while~m[x]:m[x],x=-1,m[x];Q*=X;P+=(m[x]<0)*P*Q
  t+=P//X**2**~-n%X;c+=1
 print(t//c);n+=1
```

**How it works**

- NP-equivalence lets the hyperoctahedral group B_n (permute the n inputs,
  negate any of them) act on the 2ⁿ input points. A balanced function is a
  set of 2ⁿ⁻¹ points, and it is fixed by β exactly when it is a union of
  whole cycles of β. Burnside's lemma: a(n) = (1/(2ⁿ·n!))·Σ_β [x^(2ⁿ⁻¹)]
  Π_cycles (1 + x^length).
- `for*m,p in product(range(2**n),permutations(range(n)))` runs over the
  2ⁿ·n! pairs (s, σ) with m starting as `[s]`; doubling the list with
  `y^1<<w` for each coordinate w makes m[x] = s ⊕ σ̂(x), the point map of
  β (as in [A000654](../A000654/)).
- The subset-sum polynomial is one big integer with x = X = 2^(2ⁿ): each
  coefficient counts unions of cycles, at most C(2ⁿ, 2ⁿ⁻¹) < X, so digits
  never carry. The walk (`while~m[x]`, marking visited points −1) makes L
  steps on a cycle of length L and none on a visited point; `Q` picks up
  one factor X per step, and on the last step of a cycle (where `m[x]`
  becomes −1) `P+=(m[x]<0)*P*Q` multiplies P by 1 + X^L.
- `P//X**2**~-n%X` is the coefficient of x^(2ⁿ⁻¹); `c` counts the group
  elements.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- Brute force over the 2ⁿ·n! elements: 6 terms in about 6 s on the PC
  used, but n = 7 has 645120 elements on 128 points (a few minutes). The
  bar is 6 terms in 60 s; the b-file has 10.

## First four terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(1)…a(4) have to arrive in time.

### Python 3, 4 terms — 217 bytes

```python
from itertools import*
n=1
while 1:R=range(2**n);S={0};print(sum({*f}not in S!=S.update(frozenset(s^sum((x>>i&1)<<p[i]for i in p)for x in f)for p in permutations(R[:n])for s in R)for f in combinations(R,2**~-n)));n+=1
```

**How it works**

- A balanced function is the set of its 2ⁿ⁻¹ true points, and
  `combinations(R,2**~-n)` gives each such set once (`2**~-n` is 2ⁿ⁻¹).
- For a permutation p of the coordinates and a mask s,
  `s^sum((x>>i&1)<<p[i]for i in p)` is g(x) = s ⊕ σ̂(x), where σ̂ moves bit i
  of x to position p[i]. `for i in p` visits every index once, only in
  another order, and `R[:n]` is range(n) because n < 2ⁿ. Over all p and s
  these are the 2ⁿ·n! elements of B_n, and the images g(f) of the set f are
  exactly the sets in its NP class (g(f) is the set of true points of f∘g⁻¹).
- `S` starts as {0}, a placeholder that is never a set of points, and
  collects every class met so far. `{*f}not in S!=S.update(…)` is a chained
  comparison: if f is already in S it is False and the update is skipped;
  otherwise `S.update` adds the whole class of f and returns None, and
  S != None is True. (A set looked up among frozensets is compared as a
  frozenset.) So the sum counts each class once, at its first member: a(n).
- Nothing is approximated; the count is exact for every n.

**Limits**

- a(4) = 74 takes the 12 870 balanced sets of 16 points and 74 classes of
  at most 384 images: the four terms come in about 0.3 reference seconds.
- a(5) would loop over C(32, 16) ≈ 6.0·10⁸ sets, and S would end up holding
  all of them: past a(4) the program only grows in memory until the
  interpreter gives up. The main record sums the subset-sum polynomials of
  the cycles of each group element instead.
- 217 bytes is an upper bound on the shortest valid four-term program, not a
  proof of minimality.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-07 | 263 | first entry |

**Python 3, 4 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 217 | first entry: NP classes of balanced point sets, each counted at its first member |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000721), CC BY-SA 4.0.
