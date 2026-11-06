# A139569

> A triangle of coefficients of a Chebyshev T(x,n) polynomials to make pair
> binomials by in {x,y,z} and x only polynomial reduced:
> `f(x,y,n)=Sum[CoefficientList[ChebyshevT[n, x], x][[i + 1]]*x^i*y^(n - i), {i,0, Length[CoefficientList[ChebyshevT[n, x], x]] - 1}]`;
> `p(x,y,z,n)=f(x,y,n)+f(y,z,n)+f(z,x,n)`.
> — [OEIS A139569](https://oeis.org/A139569)

Offset 1: 3, 1, 2, -1, 0, 4, 1, -6, 0, 8, 3, 0, -16, 0, 16, 1, 10, 0, -40, 0, 32, …

### Python 3 — 86 bytes

```python
a,b=[3],[1,2]
while[*map(print,a)]:a,b=b,[2*(y&x%2-2)-x for x,y in zip(a+[0,0],[1]+b)]
```

**How it works**

- Row n (n = 0, 1, 2, …) lists the coefficients of x⁰ … xⁿ in **2·Tₙ(x) + 1**,
  where Tₙ is the Chebyshev polynomial of the first kind. That is Michael
  Somos's formula on the OEIS page, and it is what the Mathematica program
  computes: with y = z = 1, f(x,1,n) = Tₙ(x) and f(1,1,n) = Tₙ(1) = 1, and the
  program adds f[x,y,n] + f[y,z,n] + f[x,z,n].
- Write Uₙ = 2Tₙ. Every coefficient of Uₙ is even, and
  Uₙ₊₁ = 2x·Uₙ − Uₙ₋₁ with U₀ = 2, U₁ = 2x. The lists `a` and `b` hold rows
  n − 1 and n **ready to print**, Rₙ = Uₙ + 1, so only the constant term is odd.
- Each new row comes from that recurrence. In `zip(a+[0,0],[1]+b)`, x runs over
  Rₙ₋₁ padded with zeros and y over Rₙ shifted one place up (the
  multiplication by x). `x%2-2` is −1 when x is odd and −2 when it is even, so
  `y&x%2-2` either keeps y or clears its lowest bit:
  - k ≥ 2: x and y are even and the result is 2y − x, the plain recurrence.
  - k = 1: y = Rₙ[0] = Uₙ[0] + 1 is odd and x is even. Clearing the bit takes
    off the +1, so the result is 2·Uₙ[0] − x, which is again the recurrence.
  - k = 0: x = Rₙ₋₁[0] = Uₙ₋₁[0] + 1 is odd, so y is kept: y is the prefix 1
    and the result is 2 − x = 1 − Uₙ₋₁[0]. Since Uₙ₊₁(0) = −Uₙ₋₁(0), that is
    Uₙ₊₁[0] + 1 = Rₙ₊₁[0], so the new row is ready to print as well.
- `while[*map(print,a)]:` prints row n one term per line. The list of `None`s
  is never empty, so the loop never stops.

**Notes**

- The name sums f(z,x,n), but the Mathematica program and the terms use
  f(x,z,n), which gives 2·Tₙ(x) + 1 above. With f(z,x,n), row 1 would be 2, 1
  instead of 1, 2.
- The b-file is synthesized from the entry: rows 0 to 10, 66 terms. The bar is
  all 66. The program was also checked against 400 rows (80 200 terms) of
  2·Tₙ(x) + 1 computed directly from the Chebyshev recurrence.
- All arithmetic is on exact integers. The largest terms grow like
  (1+√2)ⁿ (row 8 already has −512), so Python's 4300-digit int-to-str limit
  is first hit around row 11 239.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 86 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A139569), CC BY-SA 4.0.
