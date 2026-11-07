# A000626

> Number of stereoisomeric paraffins with n carbon atoms.
> — [OEIS A000626](https://oeis.org/A000626)

Offset 1: 0, 0, 0, 0, 0, 0, 4, 11, 35, 101, …

### Python 3 — 232 bytes

```python
m=2
while X:=8**m:V=U=P=[1]*3*m;R=range(m);[(V:=[1+X**k*(V[k]**3+2*V[3*k])%X**m//3for k in R]+P,U:=[1+X**k*U[k]*U[2*k]%X**m for k in R]+P)for _ in P];c=V[1]**2;w=V[2];print(((c+w)*(2-X*(c-w))-2*(U[1]+U[2]+X*U[4]))//X**~-m%X//4);m+=1
```

**How it works**

- The count is of stereoisomers of the paraffins that have an
  asymmetric carbon, a meso form counting once and an enantiomeric pair
  twice. Paraffins without an asymmetric carbon have a single steric
  form, so this is the steric count [A000628](../A000628/) minus the
  non-stereoisomeric count [A000627](../A000627/), as the entry's
  cross-reference says.
- With T(x) the steric radicals ([A000625](../A000625/)) and A(x) the
  radicals without an asymmetric carbon ([A000621](../A000621/)), the
  two pages derive
  4·A000628 = (c + w)(2 − x(c − w)) with c = T(x)², w = T(x²), and
  2·A000627 = A(x) + A(x²) + x·A(x⁴). So
  **4a(x) = (c + w)(2 − x(c − w)) − 2(A(x) + A(x²) + x·A(x⁴))**.
- Both series are packed into integers in base X = 8^m with m = n + 1,
  as in A000628: `V[k]` is T(x^k) and `U[k]` is A(x^k), updated
  together by one comprehension of pairs with
  T(x^k) = 1 + x^k(T(x^k)³ + 2T(x^(3k)))/3 and
  A(x^k) = 1 + x^k·A(x^k)·A(x^(2k)). Shifting by X^k before the cut
  `%X**m` keeps the digits of degree < m, and the `//3` is exact digit
  by digit (P(x)³ ≡ P(x³) mod 3). Entries k ≥ m stay 1 (padding `+P`).
- The printed expression is the value at X of a polynomial whose
  digits of degree < m are 4a₀,…,4aₙ; floor division and modulo read
  digit n even though the whole number is negative.
- The loop starts at m = 2 (n = 1, the offset), which also keeps
  `U[4]` inside the 4m-entry list.

**Notes**

- Base width: Tⱼ ≤ C(3j,j)/(2j+1) < 6.75ʲ (classes of plane ternary
  trees), Aⱼ ≤ Tⱼ, and aⱼ ≤ A000628(j) ≤ Tⱼ; every digit used is below
  8^m. Carries from higher digits only move up.
- Each term is recomputed from scratch. The reference file has the 36
  terms of the OEIS entry (no longer b-file there); the bar is all 36
  in 60 s. The program printed 48 terms in 60 s on a desktop PC.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 232 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000626), CC BY-SA 4.0.
