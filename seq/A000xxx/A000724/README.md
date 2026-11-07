# A000724

> Invertible Boolean functions of n variables.
> — [OEIS A000724](https://oeis.org/A000724)

Offset 1: 1, 3, 196, 3406687200, 2141364232858913975435172249600, …

### Python 3 — 139 bytes

```python
import math
f=math.factorial;n=b=c=d=1;a=0
while[print((f(N:=2**n)+(N-1<<N//2)*f(N//2)*b)//f(n)>>2*n)]:a,b,c,d=b,2*b+d+2*n*a,d,d+2*n*c;n+=1
```

**How it works**

- These are the classes of bijections f of the N = 2ⁿ points of {0,1}ⁿ
  under translations τ (x ↦ x ⊕ c) of the domain and B_n (permute and
  complement the variables) on the range (an OEIS comment). The pair
  (τ, β) fixes f when f∘τ∘f⁻¹ = β, and the number of such f is
  [τ, β have the same cycle type on the points] times the centralizer
  order of τ in S_N.
- τ = 1 is matched only by β = 1: N! maps. Each of the N − 1 other
  translations is a fixed-point-free involution, with centralizer
  2^(N/2)·(N/2)!, matched by the F_n elements of B_n that act on the points
  as fixed-point-free involutions. Burnside:
  a(n) = (N! + (N−1)·2^(N/2)·(N/2)!·F_n) / (4ⁿ·n!), Sean Irvine's formula
  in the OEIS entry.
- β = (σ, complement mask c) is an involution when σ is one and c is equal
  on the two ends of each 2-cycle; it has no fixed point exactly when c
  complements some fixed coordinate of σ. So F_n = I_n − J_n, where
  I_n = involutions of B_n (e.g.f. e^(x²+2x)) and J_n (e.g.f. e^(x²+x))
  counts the ones with c = 0 on the fixed coordinates. Both obey
  u(n+1) = y·u(n) + 2n·u(n−1), with y = 2 and 1, so
  F(n+1) = 2F(n) + J(n) + 2n·F(n−1).
- `a,b,c,d` hold F(n−1), F(n), J(n−1), J(n), starting from 0, 1, 1, 1 at
  n = 1. `N-1<<N//2` is (N−1)·2^(N/2), `N:=2**n` is set inside the print,
  and `//f(n)>>2*n` divides by n!·4ⁿ.

**Notes**

- Exact integers. The formula matches the 6 b-file terms and the brute
  force Burnside sum (as in [A000725](../A000725/)) for n ≤ 6.
- a(11) has about 5880 digits, past CPython's 4300-digit int-to-str limit,
  so the program prints 10 terms and stops with a `ValueError` (an
  interpreter limit). The b-file has 6 terms; all are the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 139 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000724), CC BY-SA 4.0.
