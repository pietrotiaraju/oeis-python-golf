# A000647

> Alkyl naphthalenes C_{n+10} H_{2n+8} with n+10 carbon atoms.
> — [OEIS A000647](https://oeis.org/A000647)

Offset 0: 1, 2, 12, 32, 110, 310, 920, 2558, 7177, 19660, …

### Python 3 — 159 bytes

```python
m=1
while X:=8**m:V=P=[1]*3*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%X**m//6for k in range(m)]+P for _ in P];print((V[1]**8+3*V[2]**4)//X**~-m%X//4);m+=1
```

**How it works**

- r(x) counts alkyl radicals ([A000598](../A000598/)), the empty one
  (a hydrogen) included: r = 1 + x(r(x)³ + 3r(x)r(x²) + 2r(x³))/6.
- Naphthalene has eight substitution sites, and its symmetries move them
  with cycle index (p₁⁸ + 3p₂⁴)/4, so by Pólya the g.f. is

  **a(x) = (r(x)⁸ + 3r(x²)⁴)/4.**
- Power series are packed into big integers in base X = 8^m with
  m = n + 1, as in [A000200](../A000200/) and [A000628](../A000628/):
  `V[k]` is r(x^k) at x = X, modulo X^m, so `V[2*k]` and `V[3*k]` are
  r(x^(2k)) and r(x^(3k)) with no substitution, and the entries k ≥ m
  stay 1, which is right modulo x^m (the padding `+P`). Each pass applies
  the equation of r(x^k); the shift by X^k comes before the cut
  `%X**m`, every digit left is a multiple of 6, so `//6` is exact digit
  by digit. Each pass fixes at least one more digit; 3m passes are more
  than enough.
- `V[1]**8+3*V[2]**4` is the value at X of a polynomial whose digits of
  degree < m are 4a₀, …, 4aₙ; `//X**~-m%X` reads digit n and `//4`
  gives aₙ.

**Notes**

- Base width: a rooted ternary tree with j ≥ 1 nodes is fixed by its
  preorder list of child counts (letters 0–3, the last one 0), so there
  are at most 4^(j−1). An ordered 8-tuple of radicals with d atoms in all
  is fixed by which entries are empty and the concatenated lists (a list
  ends exactly where its tree is complete), so there are at most
  2⁸·4^d, and a_d, a count of orbits of such tuples, is no larger. The
  answer digits 4a_d ≤ 2¹⁰·4^d are below 8^(n+1) for d ≤ n once n ≥ 8;
  the terms n ≤ 7 are checked against the b-file. The digits of the
  update are at most 6·4^(n−1). Carries from higher digits only move up.
- Each term is recomputed from scratch with integers of about 3m² bits.
  The reference file has the 27 terms of the OEIS entry (no longer
  b-file there); the bar is all 27 in 60 s, which takes about a second.
  The program printed 42 terms in 13 s on a desktop PC.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 159 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000647), CC BY-SA 4.0.
