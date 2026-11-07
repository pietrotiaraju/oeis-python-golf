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

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 263 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000721), CC BY-SA 4.0.
