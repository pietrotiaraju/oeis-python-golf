# A000671

> Number of boron trees with n nodes, i.e. n-node rooted trees with degree <= 3 at root and out-degree <= 2 elsewhere.
> — [OEIS A000671](https://oeis.org/A000671)

Offset 0: 0, 1, 1, 2, 4, 7, 14, 29, 60, 127, …

### Python 3 — 154 bytes

```python
m=1
while X:=4**m:V=P=[1]*3*m;[V:=[1+X**k*(V[k]**2+V[2*k])%X**m//2for k in range(m)]+P for _ in P];print(X*(V[1]**3+3*V[1]*V[2]+2*V[3])//X**~-m%X//6);m+=1
```

**How it works**

- B(x) = 1 + x(B(x)² + B(x²))/2 counts rooted trees in which every node
  has at most two children, the empty tree included (the
  Wedderburn–Etherington numbers A001190, shifted by one). A boron tree
  is a root with an unordered triple of such branches, so

  **a(x) = x·Z(S₃)(B) = x(B(x)³ + 3B(x)B(x²) + 2B(x³))/6.**
- Power series are packed into big integers in base X = 4^m with
  m = n + 1, as in [A000200](../A000200/): `V[k]` is B(x^k) at x = X,
  modulo X^m, so `V[2*k]` is B(x^(2k)) with no substitution, and the
  entries k ≥ m stay 1, which is right modulo x^m (the padding `+P`).
  Each pass applies the equation of B(x^k); the shift by X^k comes before
  the cut `%X**m`, every digit left is even (P(x)² ≡ P(x²) mod 2), so
  `//2` is exact digit by digit. Each pass fixes at least one more digit;
  3m passes are more than enough.
- `X*(…)` is the value at X of a polynomial whose digits of degree < m
  are 6a₀, …, 6aₙ; `//X**~-m%X` reads digit n and `//6` gives aₙ
  (a₀ = 0 comes out by itself).

**Notes**

- Base width: a rooted tree with j ≥ 2 nodes is fixed by its preorder
  list of child counts, the last one 0. With out-degrees ≤ 2 that gives
  at most 3^(j−1) trees, so the update digits are at most 2·3^(n−1); for
  a boron tree the root's count is 0–3, so a_d ≤ 4·3^(d−2) and the
  answer digits 6a_d stay below 4^(d+1). Carries from higher digits only
  move up, so the low digits are exact for every n.
- Each term is recomputed from scratch with integers of about 2m² bits;
  the time grows about like n⁶. The b-file has 201 terms; the program
  printed 66 of them in 60 s on a desktop PC, and the bar is 50 terms in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 154 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000671), CC BY-SA 4.0.
