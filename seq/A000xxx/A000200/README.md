# A000200

> Number of bicentered hydrocarbons with n atoms.
> — [OEIS A000200](https://oeis.org/A000200)

Offset 0: 0, 0, 1, 0, 1, 1, 3, 3, 9, 15, 38, 73, 174, 380, 915, 2124, …

### Python 3 — 163 bytes

```python
m=1
while B:=4**m:V=P=[1]*3*m;print((sum((V[1]-(V:=[1+B**k*(V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%B**m//6for k in range(m)]+P)[1])**2for _ in P)+V[2])//B**~-m%B//2);m+=1
```

**How it works**

The count is over carbon skeletons (trees with all degrees ≤ 4) whose
center is an edge. Cut that edge and the tree falls into two rooted
ternary trees of the same height, so bicentered trees are unordered pairs
of rooted ternary trees of equal height (Cayley; Rains and Sloane,
[On Cayley's enumeration of alkanes](https://arxiv.org/abs/math/0207176)):

- Let T_h(x) count rooted ternary trees of height ≤ h, the empty tree
  included, by number of nodes. Then T₋₁ = 1 and
  **T_h = 1 + x·S₃(T_{h−1})**, with S₃(F) = (F(x)³ + 3F(x)F(x²) + 2F(x³))/6,
  the cycle index of S₃ (three unordered branches).
- E_h = T_h − T_{h−1} counts trees of height exactly h, and an unordered
  pair of them is counted by (E_h(x)² + E_h(x²))/2. So

  **a(x) = ½ Σ_{h≥0} E_h(x)² + ½ (T(x²) − 1),**

  because the E_h(x²) telescope to T(x²) − 1.
- Power series are packed into big integers in base B = 4^m, with
  m = n + 1. `V[k]` holds T_h(x^k), so `V[2*k]` and `V[3*k]` are F(x²) and
  F(x³) without any substitution. Entries with k ≥ m stay 1, which is right
  modulo x^m (that is the padding `+P`).
- The shift by x^k comes before the cut: `B**k*(…)%B**m` keeps exactly the
  digits of degree ≤ n, and every one of them is a multiple of 6, so the
  floor division by 6 is exact and nothing above xⁿ leaks into it. The
  update leaves V[0] as junk, but only V[0] ever reads V[0].
- `(V[1]-(V:=…)[1])**2` reads the old T_{h−1}(x), builds the new list, and
  squares the difference E_h(x). The generator runs 3m times, more than
  the height ⌊n/2⌋ − 1 of either half of a tree with n atoms; after it,
  `V[2]` is T(x²) up to xⁿ.
- `//B**~-m%B` reads off the coefficient of xⁿ, which is 2a(n) (for n = 0
  it is the constant 1 of T(x²), and `//2` turns it into 0).

**Why the base is wide enough**

A rooted ternary tree with j nodes is fixed by the child counts in
preorder, so there are t(j) ≤ 4^(j−1) of them. Every digit that matters
stays below B = 4^(n+1):

- the digits of degree ≤ n − k of the S₃ numerator are 6 times a count of
  trees with at most n nodes: ≤ 6·4^(n−1);
- the digits of degree ≤ n of ΣE_h² count ordered pairs of trees with d
  nodes in all, and hanging such a pair under a new root is at most
  2-to-1 onto trees with d + 1 nodes, so they are ≤ 2·4^d; T(x²) adds
  ≤ 4^(d/2).

Carries out of higher digits only move up, so the low digits are exact
for every n.

**Golf tricks**

- Looping over m = n + 1 instead of n makes the cut `B**m`, the range
  `range(m)` and the padding `[1]*3*m` two bytes shorter each, for a cost
  of two in `B**~-m`. It also makes n = 0 an ordinary case.
- `while B:=4**m:` assigns B in the loop condition (it is never 0).
- The walrus in `(V[1]-(V:=…)[1])**2` gives the difference of two
  consecutive T_h without a second variable.
- One list `P` is both the padding and the loop counter of the generator.

**Notes**

- The program prints 65 terms in a minute on a desktop PC; the bar is
  50 terms in 60 s. The b-file has 61 terms.
- Everything is recomputed from scratch for each n.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 163 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000200), CC BY-SA 4.0.
