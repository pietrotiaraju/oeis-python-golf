# A000725

> Invertible Boolean functions of n variables.
> — [OEIS A000725](https://oeis.org/A000725)

Offset 1: 1, 2, 154, 2270394624, 571030462095782973206774552784, …

### Python 3 — 320 bytes

```python
from itertools import*
n=1
while 1:
 T=[]
 for*m,p in product(range(2**n),permutations(range(n))):
  for w in p:m+=[y^1<<w for y in m];l=[];z=1
  for x in m:
   j=0
   while~x:m[x],x=-1,m[x];j+=1
   l+=j,;z*=j<1or~-j*l.count(j)
  T+=[[z]+sorted(l)]
 print(sum(k[0]*T.count(k)for k in T[:len(T)>>n])*2**n//len(T)**2);n+=1
```

**How it works**

- These are the classes of bijections f of the 2ⁿ points of {0,1}ⁿ under
  S_n (permute the variables) on the domain and B_n (permute and complement
  them) on the range (an OEIS comment). The pair (σ, β) fixes f when
  f∘σ∘f⁻¹ = β, which has z_T solutions when σ and β have the same cycle
  type T on the points (z_T = Π_L L^(c_L)·c_L!, the centralizer order in
  S_(2ⁿ)) and none otherwise. Burnside:
  a(n) = Σ_T z_T·c_S(T)·c_B(T) / (n!·2ⁿ·n!), with c_S, c_B the number of
  elements of each group of type T.
- `for*m,p in product(range(2**n),permutations(range(n)))` builds every
  element of B_n as a point map, as in [A000654](../A000654/) (S_n on both
  sides is [A000653](../A000653/), B_n on both sides A000654). The product
  runs mask-major, so the first n! entries of `T` (mask 0) are S_n.
- The cycle walk `while~x` gives j = L + 1 on a cycle of length L and j = 0
  on a visited point. Every j goes into `l` (the zeros only add N − #cycles
  zeros, which the type fixes), and `z*=j<1or~-j*l.count(j)` builds z_T,
  3 bytes under an `if j:` line.
- `T` stores `[z]+sorted(l)` for every element; the sum runs over the S_n
  entries and counts their type among all of B_n with `T.count(k)`, so
  the weight `k[0]` is z_T. len(T) = 2ⁿ·n!, so the group order is
  len(T)²/2ⁿ.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- All 6 b-file terms in about 10 s on the PC used; n = 7 has 645120 elements
  of B_7 on 128 points and takes minutes. The bar is the whole b-file.

## First three terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(1)…a(3) have to arrive in time.

### Python 3, 3 terms — 245 bytes

```python
from itertools import*
n=1
while 1:R=range(2**n);P=[[s^sum((x>>i&1)<<p[i]for i in p)for x in R]for p in permutations(R[:n])for s in R];print(len({min(tuple(a[t[y]]for y in b)for a in P for b in P[::2**n])for t in permutations(R)if t[0]<1}));n+=1
```

**How it works**

- `P` holds the 2ⁿ·n! maps g(x) = s ⊕ σ̂(x) of B_n as lists, σ̂ moving bit i
  of x to position p[i]. `for i in p` visits every index once, only in
  another order, and `R[:n]` is range(n) because n < 2ⁿ. The mask s is the
  inner loop, so the entries at multiples of 2ⁿ, `P[::2**n]`, are the n!
  plain permutations σ̂ (s = 0), the group S_n.
- `permutations(R)` gives every invertible map f of the 2ⁿ points as the
  tuple t = (f(0), f(1), …). Since y runs over b[0], b[1], …,
  `tuple(a[t[y]]for y in b)` is the tuple of a∘f∘b, with b in S_n on the
  domain and a in B_n on the range. Both are groups, so these are exactly
  the class of f.
- Its minimum is the same for every member of the class and different
  classes are disjoint, so the set of minima has one element per class.
- `if t[0]<1` only starts from bijections with f(0) = 0. Every class has
  one: composing f with the translation y ↦ y ⊕ f(0), an element of B_n on
  the range, sends 0 to 0. The minimum is still taken over the whole class,
  so every class lands in the set: its size is a(n).
- Nothing is approximated; the count is exact for every n.

**Limits**

- a(3) = 154 takes 5040 bijections × 288 pairs: the three terms come in
  about 2 reference seconds.
- a(4) would have to list 15! ≈ 1.3·10¹² bijections even with f(0) = 0. The
  main record never lists them: Burnside's lemma over cycle types, with the
  centralizer order z_T.
- 245 bytes is an upper bound on the shortest valid three-term program, not
  a proof of minimality.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-07 | 320 | first entry |

**Python 3, 3 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 245 | first entry: smallest bijection of each class, from the bijections fixing 0 |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000725), CC BY-SA 4.0.
