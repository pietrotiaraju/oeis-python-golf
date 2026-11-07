# A000678

> Number of carbon (rooted) trees with n carbon atoms = unordered 4-tuples of ternary trees.
> — [OEIS A000678](https://oeis.org/A000678)

Offset 0: 0, 1, 1, 2, 4, 9, 18, 42, 96, 229, …

### Python 3 — 185 bytes

```python
m=1
while X:=4**m:V=P=[1]*4*m;[V:=[1+X**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%X**m//6for k in range(m)]+P for _ in P];_,a,b,c,d,*_=V;print((a*~-a+X*(b*(a*a+b)//2+a*c+d))//X**~-m%X//4);m+=1
```

**How it works**

- r(x) counts rooted ternary trees ([A000598](../A000598/)), the empty
  one included: r = 1 + x·Z(S₃)(r), with Z(S₃)(r) =
  (r(x)³ + 3r(x)r(x²) + 2r(x³))/6. A carbon tree is a root atom with an
  unordered 4-tuple of such trees, so a(x) = x·Z(S₄)(r).
- Newton's recurrence 4Z(S₄) = p₁Z(S₃) + p₂Z(S₂) + p₃p₁ + p₄ and
  Z(S₃)(r) = (r − 1)/x, read off the equation of r, give

  **4a(x) = r(r − 1) + x(r(x²)·(r(x)² + r(x²))/2 + r(x)r(x³) + r(x⁴)),**

  written `a*~-a+X*(b*(a*a+b)//2+a*c+d)` with a, b, c, d = r(X^k) for
  k = 1, …, 4.
- Power series are packed into big integers in base X = 4^m with
  m = n + 1, as in [A000200](../A000200/): `V[k]` is r(x^k) at x = X,
  modulo X^m, so `V[2*k]` and `V[3*k]` are r(x^(2k)) and r(x^(3k)) with
  no substitution, and the entries k ≥ m stay 1, which is right modulo
  x^m (the padding `+P`, four times m long so that `V[4]` exists at
  m = 1). Each pass applies the equation of r(x^k); the shift by X^k
  comes before the cut `%X**m`, every digit left is a multiple of 6, so
  `//6` is exact digit by digit. Each pass fixes at least one more digit;
  4m passes are more than enough.
- The digits of degree < m of r(x)² + r(x²) are even, and X is even, so
  `X*(b*(a*a+b)//2…)` is exact modulo X^m. The digits of degree < m of
  the whole polynomial are 4a₀, …, 4aₙ; `//X**~-m%X` reads digit n and
  `//4` gives aₙ (a₀ = 0 comes out by itself).

**Notes**

- Base width: a rooted tree with j ≥ 2 nodes is fixed by its preorder
  list of child counts, the last one 0; for a carbon tree the root's
  count is 0–4 and the others 0–3, so a_d ≤ 5·4^(d−2) and the answer
  digits 4a_d stay below 4^(d+1). The digits of the update are at most
  6·4^(n−1), as in A000200. Carries from higher digits only move up, so
  the low digits are exact for every n.
- Each term is recomputed from scratch with integers of about 2m² bits;
  the time grows about like n⁶. The b-file has 61 terms; the program
  printed 56 of them in 60 s on a desktop PC, and the bar is 44 terms in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 185 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000678), CC BY-SA 4.0.
