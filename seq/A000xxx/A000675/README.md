# A000675

> Number of centered 3-valent (or boron, or binary) trees with n nodes.
> — [OEIS A000675](https://oeis.org/A000675)

Offset 0: 1, 1, 0, 1, 1, 1, 2, 4, 5, 10, 19, 36, 68, 138, 277, 581, 1218, …

### Python 3 — 165 bytes

```python
m=1
while B:=4**m:V=P=[1]*3*m;print((3-3*sum(V[1]*(V[1]-(V:=[1+B**k*(V[k]**2+V[2*k])%B**m//2for k in range(m)]+P)[1])for _ in P)+B*(V[3]-V[1]**3))//B**~-m%B//3);m+=1
```

**How it works**

The trees have all degrees ≤ 3. A tree is centered when its longest path
has an even number 2h of edges; h is the radius and the middle node the
center (Rains and Sloane, [On Cayley's enumeration of
alkanes](https://arxiv.org/abs/math/0207176), whose Mathematica program is
on the OEIS page).

- Let T_h(x) count the rooted trees of height ≤ h in which every node has
  at most 2 children, the empty tree included: T₋₁ = 1 and
  **T_h = 1 + x·S₂(T_{h−1})** with S₂(F) = (F(x)² + F(x²))/2. Let
  E_h = T_h − T_{h−1} and T = T_∞.
- Rooted at its center, a tree of radius h ≥ 1 has at most 3 branches from
  T_{h−1}, at least two of them of height exactly h − 1. All of them:
  x·S₃(T_{h−1}) − x·S₃(T_{h−2}); those with exactly one branch of height
  h − 1: E_{h−1}·(T_{h−1} − 1). Summing over h, with the single node and the
  empty tree,
  a(x) = 1 + x·S₃(T) − Σ_{g≥0} E_g·(T_g − 1).
- Two rewrites shorten it. Newton's identity
  6S₃ = F(x)³ + 3F(x)F(x²) + 2F(x³) together with x·T(x²) = 2(T − 1) − x·T²
  (from T = 1 + x·S₂(T)) gives x·S₃(T) = T(T − 1) + x(T(x³) − T³)/3, and
  T = 1 + Σ E_g turns T² − Σ E_g·T_g into 1 + Σ E_g·T_{g−1}. So

  **a(x) = 1 + Σ_{g≥0} E_g·T_{g−1} + x·(T(x³) − T(x)³)/3.**

- Power series are packed into integers in base B = 4^m, m = n + 1, as in
  [A000200](../A000200/): `V[k]` is T_h(x^k), the shift by x^k comes before
  the cut so the `//2` is exact, and the padding `+P` keeps the entries with
  k ≥ m equal to 1. `V[1]*(V[1]-(V:=…)[1])` is −T_{g−1}·E_g: the left factor
  is read before the walrus rebinds `V`.
- After the loop `V[1]` and `V[3]` are T(x) and T(x³), and the digit of xⁿ
  of 3 − 3·Σ + B·(V[3] − V[1]³) is 3a(n); `//B**~-m%B//3` reads it.

**Why the base is wide enough**

Reduction modulo B^m is a ring map from integer polynomials modulo x^m, so
any integer combination of packed series has the right residue; its digits
are the true coefficients as soon as these lie in [0, B). Here they do:
binary rooted trees with j nodes number less than 4^j (Catalan), so the
digits of the S₂ numerator and 3a(j) for j ≤ n are below 4^(n+1). Carries
from higher degrees only move up.

**Notes**

- Exact integer arithmetic, so the program is right for every n; everything
  is recomputed for each n.
- The generator runs 3m times, more than the height n − 1 a tree with n
  nodes can reach; `P` is both that counter and the padding.
- The program prints about 65 terms in 60 s on this PC; the bar is the
  whole b-file (36 terms) in 60 s, which takes about a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 165 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000675), CC BY-SA 4.0.
