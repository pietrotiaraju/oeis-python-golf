# A000628

> Number of n-node unrooted steric quartic trees; number of n-carbon alkanes C(n)H(2n+2) taking stereoisomers into account.
> — [OEIS A000628](https://oeis.org/A000628)

Offset 0: 1, 1, 1, 1, 2, 3, 5, 11, 24, 55, …

### Python 3 — 160 bytes

```python
m=1
while X:=8**m:V=P=[1]*3*m;[V:=[1+X**k*(V[k]**3+2*V[3*k])%X**m//3for k in range(m)]+P for _ in P];c=V[1]**2;w=V[2];print((c+w)*(2-X*(c-w))//X**~-m%X//4);m+=1
```

**How it works**

- T(x) counts steric radicals ([A000625](../A000625/)):
  T = 1 + x(T(x)³ + 2T(x³))/3. In space a carbon's four branches are
  moved by the rotations of the tetrahedron, the alternating group A₄,
  and turning a bond end over end is a rotation too, so a bond joins an
  unordered pair of steric radicals.
- Otter's dissimilarity count (vertex classes − edge classes +
  symmetric edges = 1 for every tree) gives
  a(x) = x·Z(A₄;T) − ((T − 1)² + T(x²) − 1)/2 + T(x²) − 1, plus 1 for
  the empty alkane, with Z(A₄) = (p₁⁴ + 8p₁p₃ + 3p₂²)/12. Replacing
  x·T·T(x³) through the equation for T removes T(x³), giving
  x·Z(A₄;T) = T(T − 1) − x(T⁴ − T(x²)²)/4, and the sum factors:

  **a(x) = S₂(T)·(1 − x·Λ²(T))**, with S₂ = (T² + T(x²))/2 and
  Λ² = (T² − T(x²))/2,

  so 4a(x) = (c + w)(2 − x(c − w)) with c = T(x)², w = T(x²).
- The series are packed into integers in base X = 8^m with m = n + 1,
  as in [A000200](../A000200/): `V[k]` is T(x^k), so `V[3*k]` is
  T(x^(3k)) with no substitution, and entries k ≥ m stay 1, which is
  right modulo x^m (the padding `+P`). Each pass applies
  T(x^k) = 1 + x^k(T(x^k)³ + 2T(x^(3k)))/3; shifting by X^k before the
  cut `%X**m` leaves only digits of degree < m, all multiples of 3
  (P(x)³ ≡ P(x³) mod 3 for every integer polynomial), so `//3` is
  exact digit by digit. Each pass fixes at least one more digit, so the
  3m passes are more than enough.
- `c` and `w` are T(x)² and T(x²) at X. `(c+w)*(2-X*(c-w))` is the
  exact value at X of a polynomial whose coefficients of degree < m are
  4a₀,…,4aₙ; floor division and modulo read digit n even though the
  whole number is negative, and `//4` gives aₙ.

**Notes**

- Base width: steric radicals are classes of plane ternary trees, so
  Tⱼ ≤ C(3j,j)/(2j+1) < 6.75ʲ, and an alkane rooted at an end carbon is
  a radical, so aⱼ ≤ Tⱼ. The digits of the update are at most 3Tₘ and
  those of the answer at most 4aₙ, all below 8^m; carries from higher
  digits only move up.
- Each term is recomputed from scratch with integers of about 3m²
  bits. The reference file has the 39 terms of the OEIS entry (no
  longer b-file there); the bar is all 39 in 60 s. The program printed
  52 terms in 60 s on a desktop PC.
- [A000626](../A000626/) = A000628 − [A000627](../A000627/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 160 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000628), CC BY-SA 4.0.
