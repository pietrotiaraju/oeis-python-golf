# A000677

> Number of bicentered trees with n nodes.
> — [OEIS A000677](https://oeis.org/A000677)

Offset 0: 0, 0, 1, 0, 1, 1, 3, 4, 11, 20, 51, 108, 267, 619, 1541, 3762, …

### Python 3 — 172 bytes

```python
import math
m=1
while B:=4**m:M=B**m;T=0;print((sum((T-(T:=B*math.prod(pow(1-B**j,-(T//B**j%B),M)for j in range(m))%M))**2for _ in[0]*m)*B//M%B+m%2*T//B**(m//2)%B)//2);m+=1
```

**How it works**

A tree is bicentered when its longest path has an odd number of edges; the
middle edge is the bicenter. Cutting it leaves two rooted trees of the same
height, so bicentered trees are unordered pairs of rooted trees of equal
height (Cayley). With the centered trees ([A000676](../A000676/)) they make
up all trees, [A000055](../A000055/).

- Let T_h(x) count rooted trees of height ≤ h by nodes: T₋₁ = 0 and
  **T_h = x·Π_j (1 − x^j)^(−t_{h−1}(j))**, where t_{h−1}(j) is the
  coefficient of x^j in T_{h−1}. E_h = T_h − T_{h−1} counts height exactly
  h, and unordered pairs of such trees are counted by (E_h(x)² + E_h(x²))/2.
  The E_h(x²) telescope to T(x²), so

  **a(x) = ½·Σ_{h≥0} E_h(x)² + ½·T(x²).**

- The packing is the one of [A000676](../A000676/): base B = 4^m with
  m = n + 1, cut modulo M = B^m, `T//B**j%B` is t_{h−1}(j) and
  `pow(1-B**j,-d,M)` is (1 − x^j)^(−d) modulo x^m.
- `(T-(T:=…))**2` is E_h(x)², and `*B//M%B` reads its coefficient of xⁿ
  after the m heights. The coefficient of xⁿ in T(x²) is t(n/2) for even n
  and 0 for odd n: `m%2*T//B**(m//2)%B` (n is even exactly when m is odd,
  and then n/2 = m//2).

**Why the base is wide enough**

Reduction modulo M is a ring map from integer polynomials modulo x^m, so
the packed result has the right residue; its digits are the true
coefficients because those lie in [0, B): rooted trees with j nodes number
at most 4^(j−1), and ordered pairs of them with d nodes in all at most
d·4^(d−2).

**Notes**

- Exact integer arithmetic, so the program is right for every n;
  everything is recomputed for each n.
- About 52 terms print in 60 s on this PC, against 201 in the b-file; the bar is
  38 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 172 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000677), CC BY-SA 4.0.
