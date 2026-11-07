# A000673

> Number of bicentered 3-valent (or boron, or binary) trees with n nodes.
> — [OEIS A000673](https://oeis.org/A000673)

Offset 0: 0, 0, 1, 0, 1, 1, 2, 2, 6, 8, …

### Python 3 — 147 bytes

```python
m=1
while B:=4**m:V=P=[1]*2*m;print((sum((V[1]-(V:=[1+B**k*(V[k]**2+V[2*k])%B**m//2for k in range(m)]+P)[1])**2for _ in P)+V[2])//B**~-m%B//2);m+=1
```

**How it works**

The count is over trees with all degrees ≤ 3 whose center is an edge.
Cut that edge and the tree falls into two rooted trees of the same
height in which every node has at most two children, so bicentered trees
are unordered pairs of such rooted trees of equal height (Rains and
Sloane, [On Cayley's enumeration of alkanes](https://arxiv.org/abs/math/0207176)).
This is [A000200](../A000200/) with binary instead of ternary branching:

- Let T_h(x) count rooted trees with out-degree ≤ 2 and height ≤ h, the
  empty tree included. Then T₋₁ = 1 and
  **T_h = 1 + x(T_{h−1}(x)² + T_{h−1}(x²))/2**.
- E_h = T_h − T_{h−1} counts trees of height exactly h, and an unordered
  pair of them is counted by (E_h(x)² + E_h(x²))/2, so

  **a(x) = ½ Σ_{h≥0} E_h(x)² + ½ (T(x²) − 1),**

  because the E_h(x²) telescope to T(x²) − 1.
- Power series are packed into big integers in base B = 4^m, with
  m = n + 1. `V[k]` holds T_h(x^k), so `V[2*k]` is T_h(x^(2k)) with no
  substitution; entries with k ≥ m stay 1, which is right modulo x^m (the
  padding `+P`). The shift by x^k comes before the cut, so `%B**m` keeps
  the digits of degree ≤ n, all even (P(x)² ≡ P(x²) mod 2), and `//2` is
  exact digit by digit.
- `(V[1]-(V:=…)[1])**2` reads the old T_{h−1}(x), builds the new list
  and squares the difference E_h(x). The generator runs 2m times, more
  than the height of either half; after it `V[2]` is T(x²) up to xⁿ.
  `//B**~-m%B` reads off the coefficient of xⁿ, which is 2a(n) (for
  n = 0 it is the constant 1 of T(x²), and `//2` turns it into 0).

**Notes**

- Base width: a rooted tree with j ≥ 1 nodes and out-degrees ≤ 2 is fixed
  by its preorder list of child counts (letters 0–2, the last one 0), so
  there are at most 3^(j−1). The update digits are at most 2·3^(n−1). An
  ordered pair of nonempty such trees with d nodes in all, hung under a
  new root, gives a tree with d + 1 nodes, at most 2-to-1, so the digits
  of ΣE_h² are at most 2·3^d; T(x²) adds at most 3^(d/2). All stay
  below 4^(d+1), and carries from higher digits only move up.
- The reference file has the 36 terms of the OEIS entry (no longer
  b-file there); the bar is all 36 in 60 s, which takes about a second.
  The program printed 71 terms in 60 s on a desktop PC.
- [A000672](../A000672/) = A000673 + A000675 (centered trees).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 147 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000673), CC BY-SA 4.0.
