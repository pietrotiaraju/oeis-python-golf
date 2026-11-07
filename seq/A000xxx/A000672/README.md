# A000672

> Number of 3-valent trees (= boron trees or binary trees) with n nodes.
> — [OEIS A000672](https://oeis.org/A000672)

Offset 0: 1, 1, 1, 1, 2, 2, 4, 6, 11, 18, …

### Python 3 — 151 bytes

```python
m=2
while X:=4**m:V=P=[1]*2*m;[V:=[1+X**k*(V[k]**2+V[2*k])%X**m//2for k in range(m)]+P for _ in P];print((3*V[1]-X*X*(V[1]**3-V[3]))//X**~-m%X//3);m+=1
```

**How it works**

- B(x) = 1 + x(B(x)² + B(x²))/2 counts rooted trees in which every node
  has at most two children, the empty tree included (A001190 shifted by
  one). Robert A. Russell's g.f. in the OEIS entry is
  a(x) = B − (B(x)² − B(x²))/2 + x·Z(S₃)(B), with
  Z(S₃)(B) = (B(x)³ + 3B(x)B(x²) + 2B(x³))/6.
- The equation of B gives x(B(x)² + B(x²)) = 2(B − 1); using it to remove
  x·B(x)B(x²) leaves

  **a(x) = (B − 1)/x − x(B(x)³ − B(x³))/3,** so
  3aₙ = 3B_{n+1} − [x^(n−1)](B(x)³ − B(x³)).
- Power series are packed into big integers in base X = 4^m, as in
  [A000200](../A000200/), but with m = n + 2 so that B_{n+1} is still a
  digit of `V[1]` (the loop starts at m = 2): `V[k]` is B(x^k) at x = X,
  modulo X^m, so `V[2*k]` is B(x^(2k)) with no substitution, and the
  entries k ≥ m stay 1 (the padding `+P`). Each pass applies the equation
  of B(x^k); the shift by X^k comes before the cut `%X**m`, every digit
  left is even (P(x)² ≡ P(x²) mod 2), so `//2` is exact digit by digit.
  Each pass fixes at least one more digit; 2m passes are more than
  enough.
- `3*V[1]-X*X*(V[1]**3-V[3])` is the value at X of a polynomial whose
  digit of degree n + 1 is 3aₙ; `//X**~-m%X` reads it and `//3` gives
  aₙ.

**Notes**

- Base width: a rooted tree with j ≥ 1 nodes and out-degrees ≤ 2 is
  fixed by its preorder list of child counts (letters 0–2, the last one
  0), so there are at most 3^(j−1) and the update digits are at most
  2·3ⁿ < 4^m. The answer polynomial has digit 3 at degree 0 and 3a_{d−1}
  at degree d; rooting a nonempty 3-valent tree at any node gives a
  boron tree ([A000671](../A000671/)), whose root has 0–3 children, so
  a_{d−1} ≤ 4·3^(d−3) for d ≥ 3 and every digit stays below 4^(d+1).
  Carries from higher digits only move up.
- Each term is recomputed from scratch with integers of about 2m² bits;
  the time grows about like n⁶. The b-file has 192 terms; the program
  printed 69 of them in 60 s on a desktop PC, and the bar is 52 terms in
  60 s.
- A000672 = [A000673](../A000673/) (bicentered) + A000675 (centered).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 151 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000672), CC BY-SA 4.0.
