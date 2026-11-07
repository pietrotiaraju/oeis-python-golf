# A000652

> Invertible Boolean functions of n variables.
> — [OEIS A000652](https://oeis.org/A000652)

Offset 0: 1, 1, 6, 924, 81738720000, 256963707943061374889193111552000, …

### Python 3 — 71 bytes

```python
F=E=k=1
while[k&k-1or print((F+(k-1)**2*E)//k//k)]:k+=1;F*=k;E*=k%2or k
```

**What is counted**

- The OEIS comment: classes of invertible maps π of V = {0,1}ⁿ, with
  N = 2ⁿ points, under the translations τ_a(x) = x ⊕ a acting on both
  sides, π ↦ τ_b∘π∘τ_a. The group (C₂)ⁿ×(C₂)ⁿ has N² elements.
- Burnside: π is fixed by (a, b) when π∘τ_a∘π⁻¹ = τ_b. For a = b = 0 all N!
  permutations qualify. If exactly one of a, b is 0, none do (the identity
  is never conjugate to a non-identity). If both are nonzero, τ_a and τ_b
  are fixed-point-free involutions (N/2 transpositions each), so they are
  conjugate, and the π that carry one to the other form a coset of the
  centralizer, of order 2^(N/2)·(N/2)!. There are (N − 1)² such pairs, so

  a(n) = (N! + (N − 1)²·2^(N/2)·(N/2)!)/N²,

  the formula in the OEIS entry.

**How it works**

- k runs through 1, 2, 3, … with F = k! and E = the product of the even
  numbers up to k (`E*=k%2or k` multiplies by k only when k is even), so
  E = 2^(k/2)·(k/2)! whenever k is even.
- When k is a power of two, `k&k-1` is 0 and the `or` prints
  (F + (k − 1)²·E)/k² for N = k. For k = 1 (n = 0) the second term vanishes
  and the result is 1, matching the single permutation of one point.
- The conditional print sits in the `while[…]` header, whose one-element
  list is always true, so no `if` and no import are needed: tracking the
  factorials by hand is 13 bytes under `from math import*` with
  `perm(N)+((N-1)**2*perm(N//2)<<N//2)` and `N*=2`.

**Notes**

- Exact integer arithmetic. a(10) has about 2630 digits and a(11) about
  5890, so Python's 4300-digit int-to-str limit ends the output with an
  error after 11 terms.
- The bar is the whole b-file, 7 terms (n ≤ 6), in 60 s; all 11 printable
  terms take well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 71 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000652), CC BY-SA 4.0.
