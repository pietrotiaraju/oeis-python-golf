# A000676

> Number of centered trees with n nodes.
> — [OEIS A000676](https://oeis.org/A000676)

Offset 0: 1, 1, 0, 1, 1, 2, 3, 7, 12, 27, 55, 127, 284, 682, 1618, 3979, …

### Python 3 — 155 bytes

```python
import math
m=1
while B:=4**m:M=B**m;T=0;print(sum((T-(T:=B*math.prod(pow(1-B**j,-(T//B**j%B),M)for j in range(m))%M))*~-T for _ in[0]*m)*B//M%B+1//m);m+=1
```

**How it works**

A tree is centered when its longest path has an even number 2h of edges;
the middle node is the center. Together with the bicentered trees
([A000677](../A000677/)) they make up all trees, [A000055](../A000055/).

- Let T_h(x) count rooted trees of height ≤ h by nodes: T₋₁ = 0 and
  **T_h = x·Π_j (1 − x^j)^(−t_{h−1}(j))**, a root with a multiset of
  subtrees of height ≤ h − 1, where t_{h−1}(j) is the coefficient of x^j in
  T_{h−1}. Let E_h = T_h − T_{h−1}.
- Rooted at its center, a tree of radius h is a rooted tree of height h
  with at least two subtrees of height h − 1. Those with exactly one such
  subtree are that subtree times a root with lower subtrees, E_{h−1}·T_{h−1}.
  So radius h contributes E_h − E_{h−1}·T_{h−1}, and summing over h,

  **a(x) = T(x) − Σ_{h≥0} E_h(x)·T_h(x)**, plus 1 for the empty tree.

- Series are packed into integers in base B = 4^m with m = n + 1 and cut
  modulo M = B^m. `T//B**j%B` is t_{h−1}(j), and `pow(1-B**j,-d,M)` is
  (1 − x^j)^(−d) modulo x^m (1 − B^j is odd, hence invertible modulo the
  power of 4). For j = 0 both the base and the exponent are 0 and
  `pow(0,0,M)` is 1. The factor `B` is the root x.
- `(T-(T:=…))*~-T` reads the old T, rebinds it, and gives
  −E_h·(T_h − 1) (`~-T` is T − 1). The generator runs m times, through
  height n, and since the E_h add up to T the sum is T − Σ E_h·T_h: a(x)
  without its constant term. `*B//M%B` reads the coefficient of xⁿ, and
  `+1//m` adds the 1 for n = 0.

**Why the base is wide enough**

Reduction modulo M is a ring map from integer polynomials modulo x^m, so
the packed result has the right residue no matter how large the
intermediate coefficients are; its digits are the true coefficients
because every coefficient read lies in [0, B). Rooted trees with j nodes
number at most 4^(j−1) (child counts in preorder), and a(j) ≤ 4^(j−1) too.

**Notes**

- Exact integer arithmetic, so the program is right for every n;
  everything is recomputed for each n.
- The powers have exponents up to 4^j, so the program slows down quickly:
  about 52 terms in 60 s on this PC, against 201 in the b-file. The bar is 38
  terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 155 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000676), CC BY-SA 4.0.
