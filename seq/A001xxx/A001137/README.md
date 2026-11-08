# A001137

> Number of black-rooted red-black trees with n internal nodes.
> — [OEIS A001137](https://oeis.org/A001137)

Offset 1: 1, 2, 2, 4, 8, 16, 33, 56, 90, 164, 330, 688, 1440, 3008, 6291, 13168, 27604, 57896, …

### Python 3 — 78 bytes

```python
n=1
while 1:n+=1;s=B=X=3**n;exec('B=(B+B*B)**2%X**-~n;s+=B;'*n);print(s//X**n)
```

**How it works**

- A red-black tree is a binary tree whose internal nodes are red or black,
  with black leaves, no red node with a red child, and the same number of
  black nodes on every path from a node down to a leaf (its black height).
  A tree with n internal nodes has n + 1 leaves, so count by leaves.
- Let B_h(x) count black-rooted trees of black height h by leaves, with
  B₀ = x (a lone leaf). Each child of a black root of height h+1 is either a
  black tree of height h (B_h) or a red node over two such trees (B_h²), so
  B_{h+1} = (B_h + B_h²)². Then a(n) = [x^(n+1)] Σ_{h≥1} B_h. The siblings:
  red roots are Σ B_h² ([A001138](../A001138/)), and both colours together
  with n − 1 internal nodes are [A001131](../A001131/), so
  A001131(n+1) = a(n) + A001138(n).
- The program works with m = n + 1 leaves (the variable `n` in the code) and
  turns polynomials into integers by putting x = X = 3^m (Kronecker
  substitution). Reducing mod X^(m+1) keeps the coefficients of x⁰…x^m
  exactly, as long as each of them is below X: they only ever carry upward.
  `exec('…'*n)` runs m rounds of `B=(B+B*B)**2%X**-~n;s+=B`, and
  `s=B=X=3**n` starts the sum with B₀ = x, which only touches the digit
  of x¹.
- Why 3^m is a safe base: every coefficient in play counts some red-black
  trees with d ≤ m leaves, so it is at most A001131(d). From the
  functional equation A(x) = x + x² + A((x+x²)²) (Hanna, in A001131) comes
  Moon's recurrence A001131(d) = Σ_k C(2k, d−2k)·A001131(k) for d ≥ 3. If
  A001131(k) < 3^k for k < d, then A001131(d) ≤ s_d = Σ_j C(j, d−j)·√3^j,
  and s_d = √3·(s_{d−1} + s_{d−2}) with s₁ = √3, s₂ = 3 + √3 gives
  s_d < √3·(3^(d−1) + 3^(d−2)) < 3^d. So every coefficient is below 3^d ≤ X.
- A tree of black height h has at least 2^h leaves, so only h ≤ log₂ m
  matter: m rounds are more than enough, and the later ones work on 0.
  Since every digit of `s` is a count below X, no carry gets past digit m,
  and `s//X**n` reads that digit with no `%X`.

**Notes**

- Base 2^m would print `s>>n*n` (2 bytes shorter) but is wrong: the counts
  grow like 2.14^m, and that version fails from a(79) on. Base 4^m with
  `s>>2*n*n` is right but 1 byte longer.
- Moon's recurrence for this sibling, b(m) = Σ_k C(2k, m−2k)·b(k) with
  b(1) = 1 and a(n) = b(n+1) (from Σ_{h≥0} B_h = x + the same sum at
  (x+x²)²), is `from math import*` / `a=[0,n:=1]` /
  `while 1:n+=1;a+=sum(comb(2*m,n-2*m)*a[m]for m in range(n//2+1)),;print(a[n])`:
  105 bytes, but it prints the whole b-file in about a second.
- The integers have about 1.6·m² bits and each term starts again from
  scratch, so the program slows down fast: 200 terms in 12 s and 282 terms
  in 60 s here.
- The b-file has 900 terms (Alois P. Heinz); the bar is 220 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 78 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001137), CC BY-SA 4.0.
