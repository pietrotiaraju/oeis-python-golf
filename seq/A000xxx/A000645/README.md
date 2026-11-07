# A000645

> Number of alkyls X^{II} C_n H_{2n+1} Y with n carbon atoms.
> — [OEIS A000645](https://oeis.org/A000645)

Offset 0: 1, 2, 4, 10, 25, 64, 166, 437, 1157, 3087, …

### Python 3 — 175 bytes

```python
m=1
while X:=9**m:V=P=[1]*3*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%X**m//6for k in range(m)]+P for _ in P];print(2*V[1]*pow(2-X*(V[1]**2+V[2]),-1,X**m)//X**~-m%X);m+=1
```

**How it works**

- r(x) counts alkyl radicals ([A000598](../A000598/)), the empty one
  (a hydrogen) included: r = 1 + x(r(x)³ + 3r(x)r(x²) + 2r(x³))/6.
  The OEIS g.f. is A(x) = r(x)/(1 − G(x)) with
  G(x) = x(r(x)² + r(x²))/2 the g.f. of A000642, that is

  **A(x) = 2r(x) / (2 − x(r(x)² + r(x²))).**
- Power series are packed into big integers in base X = 9^m with
  m = n + 1, as in [A000200](../A000200/) and [A000628](../A000628/):
  `V[k]` is r(x^k) at x = X, modulo X^m, so `V[2*k]` and `V[3*k]` are
  r(x^(2k)) and r(x^(3k)) with no substitution, and the entries k ≥ m
  stay 1, which is right modulo x^m (the padding `+P`). Each pass applies
  the equation of r(x^k); the shift by X^k comes before the cut
  `%X**m`, every digit left is a multiple of 6, so `//6` is exact digit
  by digit. Each pass fixes at least one more digit; 3m passes are more
  than enough.
- The division is a modular inverse. A(x)·(2 − x(r² + r(x²))) = 2r(x)
  holds with integer coefficients, so evaluating the truncations at X
  gives A(X)·D ≡ 2V₁ (mod X^m) with D = 2 − X(V₁² + V₂). The base is
  odd, D ≡ 2 (mod 3) is a unit modulo X^m = 9^(m²), and
  `2*V[1]*pow(D,-1,X**m)` is A(X) modulo X^m. `//X**~-m%X` reads the
  digit of degree n.

**Notes**

- Base width: a rooted ternary tree with j ≥ 1 nodes is fixed by its
  preorder list of child counts (letters 0–3, the last one 0), so there
  are at most 4^(j−1). An ordered k-tuple of radicals with d atoms in all
  is fixed by which entries are empty and the concatenated lists (a list
  ends exactly where its tree is complete): at most 2^k·4^d. Unordered
  pairs are at most ordered ones, so A(x) ≤ Σⱼ xʲ r(x)^(2j+1)
  coefficientwise and Aₙ ≤ 2(n+1)·4ⁿ < 9^(n+1). The digits of the update
  are at most 6·4^(n−1). Carries from higher digits only move up.
- Each term is recomputed from scratch with integers of about 3.2m²
  bits. The reference file has the 28 terms of the OEIS entry (no longer
  b-file there); the bar is all 28 in 60 s, which takes about a second.
  The program printed 38 terms in 12 s on a desktop PC.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 175 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000645), CC BY-SA 4.0.
