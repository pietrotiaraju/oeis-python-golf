# A000633

> Number of acyclic quaternary ammonium ions with n carbon atoms.
> — [OEIS A000633](https://oeis.org/A000633)

Offset 4: 1, 1, 3, 7, 18, 42, 109, 269, 691, 1759, …

### Python 3 — 194 bytes

```python
m=6
while X:=9**m:V=P=[1]*3*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%X**m//6for k in range(m)]+P for _ in P];print((8*(V[1]-1)**2-X*((V[1]**2+V[2])**2-2*V[2]**2-2*V[4]))//X**~-m%X>>3);m+=1
```

**How it works**

- B(x) = 1 + x·S₃(B) counts alkyl radicals with B₀ = 1 for a hydrogen
  ([A000598](../A000598/)), S₃(F) = (F(x)³ + 3F(x)F(x²) + 2F(x³))/6. The
  nitrogen carries four nonempty radicals: a(n) = [xⁿ] S₄(B − 1), the
  entry's formula.
- Multisets of four from {H} ∪ radicals that contain no H:
  S₄(B − 1) = S₄(B) − S₃(B), and S₃(B) = (B − 1)/x. The identity
  x·S₄(B) = B(B − 1) − x·Λ²(S₂(B)) (h₁h₃ = h₄ + e₂[h₂], see
  [A000602](../A000602/)) then gives

  **x·a(x) = (B − 1)² − x·Λ²(G), G = S₂(B) = (B² + B(x²))/2**,

  Λ²(G) = (G² − G(x²))/2. With f = 2G = B(x)² + B(x²):
  8x·a(x) = 8(B − 1)² − x(f² − 2B(x²)² − 2B(x⁴)).
- The series are packed into integers in base X = 9^m, as on the
  [A000602](../A000602/) page: `V[k]` is B(x^k) evaluated at X and cut
  below X^m, so `V[2*k]`, `V[3*k]` are B(x^(2k)), B(x^(3k)) with no
  substitution, and the padding entries `+P` (k ≥ m) are 1, which is right
  modulo x^m. Each pass applies B(x^k) = 1 + x^k·S₃(B)(x^k); shifting by
  X^k before the cut keeps only digits of degree < m, all multiples of 6,
  so `//6` is exact digit by digit. Each pass fixes at least one more
  digit, and there are more than m passes.
- m = n + 2: the printed expression is the value at X of a polynomial
  whose digits of degree < m are 0, 8a₀, …, 8aₙ; floor division and
  modulo read digit m − 1 although the number is negative, and `>>3`
  gives aₙ.

**Notes**

- Base width: a tree with child counts at most 3 is fixed by its child
  counts in preorder, so Bⱼ ≤ 4^(j−1) for j ≥ 1, and the update digits
  are at most 6Bₘ₋₁ < 9^m. The answer digits are 8aⱼ with
  aⱼ ≤ [xʲ](B − 1)⁴ ≤ [xʲ]x⁴/(1 − 4x)⁴, far below 9^m. Carries from
  higher digits only move up.
- Each term is recomputed from scratch with integers of about 3m² bits.
- The reference file has the 31 terms of the OEIS b-file;
  the bar is all 31 in 60 s (it needs about 7 s here and printed 45 terms in 60 s).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 194 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000633), CC BY-SA 4.0.
