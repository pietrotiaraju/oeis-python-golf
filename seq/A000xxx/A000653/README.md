# A000653

> Invertible Boolean functions of n variables.
> — [OEIS A000653](https://oeis.org/A000653)

Offset 1: 2, 7, 1172, 36325278240, 18272974787063551687986348306336, …

### Python 3 — 291 bytes

```python
from itertools import*
n=1
while 1:
 D={};a=c=0
 for p in permutations(range(n)):
  m=[0];l=[];z=1;c+=1
  for w in p:m+=[y+2**w for y in m]
  for x in m:
   j=0
   while~x:m[x],x=-1,m[x];j+=1
   if j:l+=j,;z*=~-j*l.count(j)
  k=(*sorted(l),);D[k]=d=D.get(k,0)+z;a+=d+d-z
 print(a//c//c);n+=1
```

**What is counted**

- The OEIS comment: classes of invertible maps π of V = {0,1}ⁿ (N = 2ⁿ
  points) when the variables are permuted on the domain and on the range,
  π ↦ σ̂∘π∘τ̂⁻¹ for σ, τ in S_n, where σ̂ moves bit i of a point to
  position σ(i).
- Burnside over the n!² pairs: π is fixed by (σ, τ) when π∘τ̂∘π⁻¹ = σ̂.
  That needs σ̂ and τ̂ to have the same cycle type T on the N points, and
  then exactly z_T = Π_j j^(c_j)·c_j! permutations π do it (c_j cycles of
  length j; z_T is the order of the centralizer). Writing N_T for the
  number of σ with σ̂ of type T,

  a(n) = Σ_T N_T²·z_T / n!².

**How it works**

- For each permutation p of the n coordinates, `m` starts as `[0]` and
  coordinate w doubles it with `y+2**w`, so m[x] is x with bit i moved to
  position p[i]: m is σ̂ as a list (bit p[i] is still clear in every y, so
  `+` is `|`, one byte shorter).
- Cycle walk: `for x in m` reads each position in turn. A visited position
  reads −1 and `while~x` stops at once (j = 0). Otherwise the walk marks the
  cycle with −1 and ends when it reads a marked point, after L + 1 steps for
  a cycle of length L. So every cycle appends j = L + 1 to l exactly once
  (the shift by one does not change the sorted key) and multiplies z by
  L·(number of cycles of length L so far), which builds z_T.
- The key is the sorted tuple of l. D[key] holds N_T·z_T so far; one more
  element of type T adds 2·(old value) + z_T to Σ N_T²·z_T, which is
  `d+d-z` with d the new value. c counts the n! elements.

**Notes**

- n!·2ⁿ steps of the walk: the whole b-file (n ≤ 8) takes about 15 s here,
  n = 9 a few minutes. Every term is exact.
- a(10) has about 2630 digits and a(11) about 5880, so Python's 4300-digit
  int-to-str limit would stop the output after 10 terms.
- The bar is the whole b-file, 8 terms, in 60 s.

## First three terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(1)…a(3) have to arrive in time.

### Python 3, 3 terms — 216 bytes

```python
from itertools import*
n=1
while 1:R=range(2**n);P=[[sum((x>>i&1)<<p[i]for i in p)for x in R]for p in permutations(R[:n])];print(len({min(tuple(a[t[y]]for y in b)for a in P for b in P)for t in permutations(R)}));n+=1
```

**How it works**

- `P` holds the n! maps σ̂ as lists, σ̂[x] being x with bit i moved to
  position p[i]. `for i in p` visits every index once, only in another
  order, and `R[:n]` is range(n) because n < 2ⁿ.
- `permutations(R)` gives every invertible map π of the 2ⁿ points as the
  tuple t = (π(0), π(1), …). Since y runs over b[0], b[1], …,
  `tuple(a[t[y]]for y in b)` is the tuple of a∘π∘b.
- P is a group, so as a and b run over it these tuples are exactly the class
  {σ̂∘π∘τ̂⁻¹} of π. Its minimum is the same for every member of the class and
  different classes are disjoint, so the set of minima has one element per
  class: its size is a(n).
- Nothing is approximated; the count is exact for every n.

**Limits**

- a(3) = 1172 takes 40 320 bijections × 36 pairs (σ, τ): the three terms
  come in about 2 reference seconds.
- a(4) would have to list 16! ≈ 2.1·10¹³ bijections. The main record never
  lists them: Burnside's lemma over pairs of cycle types, with the
  centralizer order z_T, reaches all eight b-file terms.
- 216 bytes is an upper bound on the shortest valid three-term program, not
  a proof of minimality.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-07 | 291 | first entry |

**Python 3, 3 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 216 | first entry: smallest bijection of each class, over all bijections |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000653), CC BY-SA 4.0.
