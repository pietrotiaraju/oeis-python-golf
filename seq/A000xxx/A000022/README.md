# A000022

> Number of centered hydrocarbons with n atoms.
> — [OEIS A000022](https://oeis.org/A000022)

Offset 0: 0, 1, 0, 1, 1, 2, 2, 6, 9, 20, 37, 86, 181, 422, 943, 2223, …

### Python 3 — 200 bytes

```python
m=1
while B:=4**m:V=P=[1]*4*m;print((-sum(V[1]*(V[1]-(V:=[1+B**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%B**m//6for k in range(m)]+P)[1])for _ in P)-B//8*((V[1]**2+V[2])**2-2*V[2]**2-2*V[4]))//B**~-m%B);m+=1
```

**How it works**

The count is over carbon skeletons (trees with all degrees ≤ 4) whose
center is a single atom. It follows the method of Rains and Sloane,
[On Cayley's enumeration of alkanes](https://arxiv.org/abs/math/0207176),
the one behind the Mathematica program on the entry, and then rewrites
their formula so that it needs no F(x³) and no division by 24:

- Let T_h(x) count rooted ternary trees of height ≤ h, the empty tree
  included, by number of nodes. Then T₋₁ = 1 and
  **T_h = 1 + x·S₃(T_{h−1})**, where S₃(F) = (F(x)³ + 3F(x)F(x²) + 2F(x³))/6
  is the cycle index of S₃ (three unordered branches). Write T = T_∞ and
  E_h = T_h − T_{h−1} (trees of height exactly h).
- Rooted at its center, a centered tree is a carbon with four unordered
  branches of which at least two reach the greatest height. All carbons
  with four branches give x·S₄(T); the bad ones have one branch of height
  exactly h and three below it, so
  a(x) = x·S₄(T) − Σ_h E_h·(T_h − 1).
- Newton's identities 4S₄ = F·S₃ + F(x²)S₂ + F(x³)S₁ + F(x⁴) and
  3S₃ = F·S₂ + F(x²)F + F(x³), together with x·S₃(T) = T − 1, eliminate
  F(x³): **x·S₄(T) = T(T − 1) − x·Λ²(S₂(T))**, where S₂(F) = (F² + F(x²))/2
  and Λ²(G) = (G² − G(x²))/2 counts pairs of distinct items.
- Since T² − 1 = Σ_h E_h(T_h + T_{h−1}), the two parts combine into

  **a(x) = Σ_h E_h·T_{h−1} − x·Λ²(S₂(T)),**

  and 8Λ²(S₂(T)) = (T² + T(x²))² − 2T(x²)² − 2T(x⁴).
- Power series are packed into big integers in base B = 4^m, with
  m = n + 1. `V[k]` holds T_h(x^k), so `V[2*k]` and `V[3*k]` are F(x²) and
  F(x³) without any substitution; entries with k ≥ m stay 1, which is right
  modulo x^m (that is the padding `+P`).
- The shift by x^k comes before the cut: `B**k*(…)%B**m` keeps exactly the
  digits of degree ≤ n, all multiples of 6, so the floor division by 6 is
  exact. The update leaves V[0] as junk, but only V[0] reads V[0].
- `V[1]*(V[1]-(V:=…)[1])` is T_{h−1}·(T_{h−1} − T_h) = −E_h·T_{h−1}: it reads
  the old T_{h−1}(x) twice, then builds the new list. The generator runs
  4m times, more than the height of any tree with n atoms.
- `B//8` is x/8. The coefficients of degree ≤ n of the bracket are
  multiples of 8, so B/8 times it agrees with x·Λ² up to xⁿ, and the
  digits above only add multiples of B^(n+1). For n = 0, `B//8` is 0,
  which is right because the term starts at x¹.
- `//B**~-m%B` reads off the coefficient of xⁿ. The sum and the product
  are exact values of polynomials at B, so the only digits that have to
  fit are those of the answer.

**Why the base is wide enough**

A tree whose nodes have at most 3 children (the root at most 4) is fixed
by its child counts in preorder, so there are at most 4^(j−1) rooted
ternary trees with j nodes and at most 5·4^(j−2) centered trees with
j ≥ 2 atoms. The digits of degree ≤ n − k of the S₃ numerator are at most
6·4^(n−1), and a(n) is at most 5·4^(n−2); both are below B = 4^(n+1).
Carries from higher digits only move up.

**Golf tricks**

- Looping over m = n + 1 makes the cut `B**m`, the range `range(m)` and
  the padding `[1]*4*m` short, and n = 0 an ordinary case.
- `while B:=4**m:` assigns B in the loop condition.
- The sum comes first in the printed expression, so `V[1]`, `V[2]` and
  `V[4]` after it already hold the final T(x), T(x²) and T(x⁴): no
  variables for them.
- `[1]*4*m` (not 3) keeps `V[4]` in range when n = 0.

**Notes**

- The program prints 58 terms in a minute on a desktop PC; the bar is
  40 terms in 60 s. The b-file has 61 terms.
- The same packing gives [A000200](../A000200/) (bicentered).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 247 | first entry |
| 2026-11-05 | Python 3 | 200 | shift before the cut, base 4^(n+1), a = ΣE_h·T_{h−1} − x·Λ²(S₂(T)) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000022), CC BY-SA 4.0.
