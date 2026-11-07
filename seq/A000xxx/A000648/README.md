# A000648

> Number of alkyls C_{n+15} H_{2n+10} (Anthr.) with n carbon atoms.
> — [OEIS A000648](https://oeis.org/A000648)

Offset 0: 1, 3, 18, 61, 225, 716, 2272, 6826, 20238, 58552, …

### Python 3 — 173 bytes

```python
m=1
while X:=8**m:V=P=[1]*3*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%X**m//6for k in range(m)]+P for _ in P];a,b=V[1:3];print((a**10+(a*a+2*b)*b**4)//X**~-m%X//4);m+=1
```

**How it works**

- r(x) counts alkyl radicals ([A000598](../A000598/)), the empty one
  (a hydrogen) included: r = 1 + x(r(x)³ + 3r(x)r(x²) + 2r(x³))/6.
- Anthracene has ten substitution sites, and its symmetries move them
  with cycle index (p₁¹⁰ + p₁²p₂⁴ + 2p₂⁵)/4 (one symmetry fixes the
  middle sites 9 and 10 and swaps the other eight in pairs, the other two
  swap all ten in pairs), so by Pólya the g.f. is

  **a(x) = (r(x)¹⁰ + r(x)²r(x²)⁴ + 2r(x²)⁵)/4,**

  written `a**10+(a*a+2*b)*b**4` with a = r(X), b = r(X²).
- Power series are packed into big integers in base X = 8^m with
  m = n + 1, as in [A000200](../A000200/) and [A000628](../A000628/):
  `V[k]` is r(x^k) at x = X, modulo X^m, so `V[2*k]` and `V[3*k]` are
  r(x^(2k)) and r(x^(3k)) with no substitution, and the entries k ≥ m
  stay 1, which is right modulo x^m (the padding `+P`). Each pass applies
  the equation of r(x^k); the shift by X^k comes before the cut
  `%X**m`, every digit left is a multiple of 6, so `//6` is exact digit
  by digit. Each pass fixes at least one more digit; 3m passes are more
  than enough.
- The digits of degree < m of the answer polynomial are 4a₀, …, 4aₙ;
  `//X**~-m%X` reads digit n and `//4` gives aₙ.

**Notes**

- Base width: a rooted ternary tree with j ≥ 1 nodes is fixed by its
  preorder list of child counts (letters 0–3, the last one 0), so there
  are at most 4^(j−1). An ordered 10-tuple of radicals with d atoms in
  all is fixed by which entries are empty and the concatenated lists (a
  list ends exactly where its tree is complete), so there are at most
  2¹⁰·4^d, and a_d, a count of orbits of such tuples, is no larger. The
  answer digits 4a_d ≤ 2¹²·4^d are below 8^(n+1) for d ≤ n once
  n ≥ 10; the terms n ≤ 9 are checked against the b-file. The digits of
  the update are at most 6·4^(n−1). Carries from higher digits only move
  up.
- Each term is recomputed from scratch with integers of about 3m² bits.
  The reference file has the 26 terms of the OEIS entry (no longer
  b-file there); the bar is all 26 in 60 s, which takes about a second.
  The program printed 42 terms in 13 s on a desktop PC.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 173 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000648), CC BY-SA 4.0.
