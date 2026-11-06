# A000432

> Series-parallel numbers.
> — [OEIS A000432](https://oeis.org/A000432)

Offset 3: 8, 52, 288, 1424, 6648, 29700, 128800, 545600, 2269672, 9303140, …

### Python 3 — 184 bytes

```python
A=[1,n:=1]
while 1:
 B=1<<(5*n+3);S=sum(A[k]*B**k for k in range(1,n))
 print(4*(2+S)*(1+S)*pow(1-S,-5,B**n)//B**(n-1)%B)
 n+=1;A+=sum(sum(A[-d::-d])*d*A[d]for d in(1,*range(1,n)))//n,
```

**How it works**

- Write S(x)=Σₖ≥₁ s(k)xᵏ for the positive-degree series of
  [A000084](../A000084/). The generating function here is
  H(S)=4(2+S)(1+S)/(1−S)⁵. Its degree-m coefficient is the
  OEIS term a(m+3), so the code's n=m+1 is shifted from the
  sequence index by two.
- A stores s(0)=1 as an auxiliary Euler-transform value and the
  successive network counts. When appending s(n), the recurrence
  is n·s(n)=Σ_(d<n) w_d·Σⱼ≥₁ s(n−jd), with w_1=2 and
  w_d=d·s(d) for d>1, as derived on A000084.
- `(1,*range(1,n))` repeats d=1 to give its doubled weight.
  `A[-d::-d]` walks backward through s(n−d), s(n−2d), …,
  including the auxiliary s(0). Division by n is exact.
- Before that update, pack the currently needed series through
  degree m=n−1 as `S=sum(A[k]*B**k for k in range(1,n))`.
  The variable S is the integer S(B), not a floating value of
  the generating function at a small real argument.
- Since S is divisible by B, 1−S is coprime to B^(m+1).
  `pow(1-S,-5,B**n)` computes its inverse fifth power modulo
  that modulus. Multiplying by the numerator and taking
  `//B**(n-1)%B` extracts the degree-m coefficient.
- At m=0 the packed S is zero and the result is H(0)=8.
  At m=1, the coefficient is H′(0)s(1)=52, giving the next
  term. The constant auxiliary A[0] is never packed into S.

**Why the packed digit is exact**

- Every network can be represented by a plane binary expression tree
  with k leaves and series/parallel choices at its internal nodes.
  There are at most 4^(k−1) plane binary shapes and 2^(k−1)
  choices, so s(k)≤8ᵏ. Consequently S(1/32)≤Σₖ≥₁(1/4)ᵏ=1/3.
- H has nonnegative coefficients, and H(1/3)=189/2<128.
  Thus every coefficient h_j satisfies h_j·32^(−j)<128.
  Through degree m all are less than 128·32ᵐ<B, so lower
  digits cannot carry into the digit being extracted.
- Formal evaluation modulo B^(m+1) discards higher degrees. The
  denominator is invertible because its constant term is 1; its
  modular inverse therefore agrees with the truncated power-series
  inverse. Integer evaluation recovers exactly h_m.

**Notes**

- This avoids implementing polynomial multiplication and division
  explicitly: integer arithmetic and a modular inverse perform the
  truncated series calculation once the base is large enough.
- B=2^(5n+3)=256·32ᵐ is rebuilt for each degree. The input
  network list grows linearly in m; the packed numbers and modulus
  have O(m²) bits, making modular integer arithmetic the main
  cost at larger degrees.
- [A000444](../A000444/) and [A000485](../A000485/) use
  the same exact digit-extraction method on rooted-tree series.
  The proof above concerns all coefficients, not only the b-file.
- The b-file has 38 terms (indices 3 through 40). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 184 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000432), CC BY-SA 4.0.
