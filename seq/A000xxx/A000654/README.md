# A000654

> Invertible Boolean functions of n variables.
> — [OEIS A000654](https://oeis.org/A000654)

Offset 1: 1, 2, 52, 142090700, 17844701940501123640681816160, …

### Python 3 — 306 bytes

```python
from itertools import*
n=1
while 1:
 D={};a=c=0
 for*m,p in product(range(2**n),permutations(range(n))):
  for w in p:m+=[y^1<<w for y in m];l=[];z=1
  for x in m:
   j=0
   while~x:m[x],x=-1,m[x];j+=1
   if j:l+=j,;z*=~-j*l.count(j)
  k=(*sorted(l),);D[k]=d=D.get(k,0)+z;a+=d+d-z;c+=1
 print(a//c//c);n+=1
```

**What is counted**

- The OEIS comment: classes of invertible maps π of V = {0,1}ⁿ (N = 2ⁿ
  points) when the variables may be permuted and complemented on the
  domain and on the range. The group acting on each side is the
  hyperoctahedral group B_n of the 2ⁿ·n! maps g(x) = σ̂(x) ⊕ s.
- As for [A000653](../A000653/), π is fixed by (g, h) exactly when
  π∘ĥ∘π⁻¹ = ĝ, which needs equal cycle types T on the N points and then has
  z_T = Π_j j^(c_j)·c_j! solutions, so

  a(n) = Σ_T N_T²·z_T / (2ⁿ·n!)²,

  with N_T the number of g ∈ B_n of type T.

**How it works**

- `for*m,p in product(range(2**n),permutations(range(n)))` runs over the
  pairs (s, σ) with m starting as `[s]` (the starred target). Coordinate w
  doubles the list with `y^1<<w`, so m[x] = s ⊕ σ̂(x). The doubling line
  also resets l and z, harmlessly n times.
- The cycle walk, the key and the one-pass sum `D[k]=d=D.get(k,0)+z;
  a+=d+d-z` are those of [A000653](../A000653/): `while~x` stops when x
  reads a marked −1, each cycle of length L gives j = L + 1, and
  `z*=~-j*l.count(j)` builds z_T. c counts the 2ⁿ·n! elements.

**Notes**

- The work is 4ⁿ·n! walk steps: n = 6 takes about 4 s here, and n = 7
  (645,120 maps on 128 points) about two minutes. a(11) would pass Python's
  4300-digit int-to-str limit.
- The bar is 6 terms in 60 s; the b-file has 7.

## First three terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(1)…a(3) have to arrive in time.

### Python 3, 3 terms — 237 bytes

```python
from itertools import*
n=1
while 1:R=range(2**n);P=[[s^sum((x>>i&1)<<p[i]for i in p)for x in R]for p in permutations(R[:n])for s in R];print(len({min(tuple(a[t[y]]for y in b)for a in P for b in P)for t in permutations(R)if t[0]<1}));n+=1
```

**How it works**

- `P` holds the 2ⁿ·n! maps g(x) = s ⊕ σ̂(x) of B_n as lists, σ̂ moving bit i
  of x to position p[i]. `for i in p` visits every index once, only in
  another order, and `R[:n]` is range(n) because n < 2ⁿ.
- `permutations(R)` gives every invertible map π of the 2ⁿ points as the
  tuple t = (π(0), π(1), …). Since y runs over b[0], b[1], …,
  `tuple(a[t[y]]for y in b)` is the tuple of a∘π∘b. P is a group, so as a
  and b run over it these are exactly the class of π.
- Its minimum is the same for every member of the class and different
  classes are disjoint, so the set of minima has one element per class.
- `if t[0]<1` only starts from bijections with π(0) = 0. Every class has
  one: composing π with the translation y ↦ y ⊕ π(0), an element of B_n on
  the range, sends 0 to 0. The minimum is still taken over the whole class,
  so every class lands in the set: its size is a(n).
- Nothing is approximated; the count is exact for every n.

**Limits**

- a(3) = 52 takes 5040 bijections × 48² pairs, about 11.6 million tuples of
  8: the three terms come in about 10 reference seconds.
- a(4) would have to list 15! ≈ 1.3·10¹² bijections even with π(0) = 0. The
  main record never lists them: Burnside's lemma over cycle types, with the
  centralizer order z_T.
- 237 bytes is an upper bound on the shortest valid three-term program, not
  a proof of minimality.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-07 | 306 | first entry |

**Python 3, 3 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 237 | first entry: smallest bijection of each class, from the bijections fixing 0 |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000654), CC BY-SA 4.0.
