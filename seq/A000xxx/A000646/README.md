# A000646

> Number of alkyls Y^{II} C_n H_{2n+2} with n carbon atoms.
> — [OEIS A000646](https://oeis.org/A000646)

Offset 0: 1, 2, 3, 6, 13, 28, 62, 144, 338, 810, …

### Python 3 — 144 bytes

```python
m=1
while X:=8**m:V=P=[1]*3*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%X**m//6for k in range(m)]+P for _ in P];print(V[1]**2//X**~-m%X);m+=1
```

**How it works**

- r(x) counts alkyl radicals ([A000598](../A000598/)), the empty one
  (a hydrogen) included: r = 1 + x(r(x)³ + 3r(x)r(x²) + 2r(x³))/6.
  The OEIS g.f. of this sequence is **r(x)²**, an ordered pair of
  radicals on the divalent group.
- Power series are packed into big integers in base X = 8^m with
  m = n + 1, as in [A000200](../A000200/) and [A000628](../A000628/):
  `V[k]` is r(x^k) at x = X, modulo X^m, so `V[2*k]` and `V[3*k]` are
  r(x^(2k)) and r(x^(3k)) with no substitution, and the entries k ≥ m
  stay 1, which is right modulo x^m (the padding `+P`).
- Each pass applies the equation of r(x^k). The shift by X^k comes
  before the cut `%X**m`, so only digits of degree < m survive, and all
  of them are multiples of 6 (P³ + 3P·P(x²) + 2P(x³) ≡ 0 mod 6 for every
  integer polynomial P), so `//6` is exact digit by digit. Each pass
  fixes at least one more digit; the 3m passes are more than enough.
- `V[1]**2` is r(X)², and `//X**~-m%X` reads its digit of degree n.

**Notes**

- Base width: a rooted ternary tree with j ≥ 1 nodes is fixed by its
  preorder list of child counts (letters 0–3, the last one 0), so there
  are at most 4^(j−1) of them. An ordered pair of radicals with d atoms
  in all is fixed by which of the two is empty and the concatenated
  lists (a list ends exactly where its tree is complete), so the digits
  of r² are at most 4·4^d < 8^(d+1). The digits of the update are at
  most 6·4^(n−1). Carries from higher digits only move up, so the low
  digits are exact for every n.
- Each term is recomputed from scratch with integers of about 3m² bits.
  The reference file has the 30 terms of the OEIS entry (no longer
  b-file there); the bar is all 30 in 60 s. The program printed 43 terms
  in 15 s on a desktop PC.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 144 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000646), CC BY-SA 4.0.
