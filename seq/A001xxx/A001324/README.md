# A001324

> Number of equivalence classes of n-valued Post functions of 2 variables under action of semi-direct product of symmetric group S_2 and complementing group C(2,n).
> — [OEIS A001324](https://oeis.org/A001324)

Offset 2: 6, 1230, 134355076, 5960467529298425, …

With k values, the functions are the maps Z_k² → Z_k. C(2,k) shifts each
variable, (x, y) ↦ (x + a, y + b), and S₂ swaps them; the group has 2k²
elements, the maps (x, y) ↦ (x + a, y + b) and (x, y) ↦ (y + a, x + b). For
k = 2 this is the 6 classes of Boolean functions of 2 variables under
permuting and complementing inputs ([A000616](../../A000xxx/A000616/)).

### Python 3 — 124 bytes

```python
from math import*
k=2
while[print(sum(k**((g:=gcd(i,k))*k+k%(2*g)>>1)+k**(k*gcd(g,i//k))for i in range(k*k))//2//k//k)]:k+=1
```

**What is counted**

- Burnside's lemma: a(k) = Σ_g k^c(g) / (2k²), where c(g) is the number of
  cycles of g on the k² points.
- The translation by (a, b) has order k/gcd(a,b,k) and all its cycles have
  that length, so c = k·gcd(a,b,k).
- For g(x, y) = (y + a, x + b), g² is the translation by (s, s) with
  s = a + b, of order d = k/gcd(s,k), so g has order 2d. An even power g²ʲ
  (j < d) fixes all k² points only for j = 0; an odd power g²ʲ⁺¹ fixes the
  k points with x = y + a + js when (2j+1)s ≡ 0 (mod k), and none
  otherwise, and below 2d that happens only for 2j + 1 = d with d odd.
  Burnside's lemma for ⟨g⟩ gives c = (k² + k·[d odd])/(2d)
  = (gk + (k mod 2g))/2 with g = gcd(s,k), because k mod 2g is g when
  d = k/g is odd and 0 when it is even.

**How it works**

- i runs over the k² pairs a = i mod k, b = i // k. Then `g` = gcd(i,k)
  = gcd(a,k) and `gcd(g,i//k)` = gcd(a,b,k), so the second power is the
  translation term k^(k·gcd(a,b,k)).
- The first power is the swap term with s = a in place of s = a + b: each
  residue s is a for exactly k pairs and a + b for exactly k pairs, so the
  sum over all pairs is the same.
- `//2//k//k` divides by the group order 2k²; Burnside's lemma makes it
  exact. The loop starts at the offset k = 2.

**Notes**

- Writing the translation term first, as `k**(k*gcd(i,k,i//k))`, is 126
  bytes.
- a(51) has 4438 digits, so printing it stops the program with Python's
  4300-digit int-to-str limit after 49 terms (k = 2 to 50); they take a
  fraction of a second.
- The b-file is synthesized from the 7 terms of the entry; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 124 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001324), CC BY-SA 4.0.
