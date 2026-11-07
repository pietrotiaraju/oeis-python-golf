# A000602

> Number of n-node unrooted quartic trees; number of n-carbon alkanes C(n)H(2n+2) ignoring stereoisomers.
> — [OEIS A000602](https://oeis.org/A000602)

Offset 0: 1, 1, 1, 1, 2, 3, 5, 9, 18, 35, …

### Python 3 — 185 bytes

```python
m=1
while X:=9**m:V=P=[1]*4*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%X**m//6for k in range(m)]+P for _ in P];f=V[1]**2+V[2];print((4*f-X*(f*f-2*V[2]**2-2*V[4]))//X**~-m%X//8);m+=1
```

**How it works**

- B(x) counts alkyl radicals ([A000598](../A000598/)):
  B = 1 + x·S₃(B), S₃(F) = (F(x)³ + 3F(x)F(x²) + 2F(x³))/6. The entry
  gives the alkanes as a(x) = B − (B² − B(x²))/2 + x·S₄(B) (Otter's
  dissimilarity count).
- Newton's identities turn x·S₄(B) into B(B − 1) − x·Λ²(S₂(B)), with
  S₂(F) = (F² + F(x²))/2 and Λ²(G) = (G² − G(x²))/2 (the identity used
  on the [A000022](../A000022/) page). Everything collapses to

  **a(x) = G − x·Λ²(G), G = S₂(B)**,

  and with f = 2G = B(x)² + B(x²):
  8a(x) = 4f − x(f² − 2B(x²)² − 2B(x⁴)).
- The series are packed into integers in base X = 9^m with m = n + 1,
  as in [A000200](../A000200/): `V[k]` is B(x^k), so `V[2*k]` and
  `V[3*k]` are B(x^(2k)), B(x^(3k)) with no substitution, and entries
  k ≥ m stay 1, which is right modulo x^m (the padding `+P`). Each pass
  applies B(x^k) = 1 + x^k·S₃(B)(x^k); shifting by X^k before the cut
  `%X**m` keeps only digits of degree < m, all multiples of 6, so `//6`
  is exact digit by digit. Each pass fixes at least one more digit;
  4m passes are more than enough.
- The printed expression is the value at X of a polynomial whose
  digits of degree < m are 8a₀,…,8aₙ; floor division and modulo read
  digit n even though the whole number is negative, and `//8` gives aₙ.

**Notes**

- Base width: a tree with child counts at most 3 is fixed by its child
  counts in preorder, so Bⱼ ≤ 4^(j−1) for j ≥ 1, and an alkane rooted
  at an end carbon is a radical, so aⱼ ≤ Bⱼ. The update digits are at
  most 6Bₘ and the answer digits at most 8aₙ (8 when n = 0, hence base
  9 rather than 8), all below 9^m. Carries from higher digits only move
  up.
- Each term is recomputed from scratch with integers of about 3m²
  bits, so the program is slow but short: it printed 47 terms in 60 s
  on a desktop PC. The reference file has the 1001 terms of the OEIS
  b-file; the bar is 35 terms in 60 s. A list version with cached
  convolutions (215 bytes) prints the whole b-file in seconds.
- A000602 = [A000022](../A000022/) + [A000200](../A000200/) for n > 0
  (centered plus bicentered); the steric version is
  [A000628](../A000628/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 185 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000602), CC BY-SA 4.0.
