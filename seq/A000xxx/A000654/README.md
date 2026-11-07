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

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 306 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000654), CC BY-SA 4.0.
