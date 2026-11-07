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

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 320 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000725), CC BY-SA 4.0.
