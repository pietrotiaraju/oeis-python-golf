# A000220

> Number of asymmetric trees with n nodes (also called identity trees).
> — [OEIS A000220](https://oeis.org/A000220)

Offset 1: 1, 0, 0, 0, 0, 0, 1, 1, 3, 6, 15, 29, 67, 139, 310, 667, …

### Python 3 — 143 bytes

```python
R=[n:=-1,0,1]
while[print(sum(map(int.__mul__,R,R[::-1]),R[-n])//-2)]:R+=0,sum(d*(R[-d-d]-R[-d])*sum(R[d-~d:0:d+d])for d in range(n,0))//n;n-=1
```

**How it works**

- Let b(n) count rooted identity trees
  ([A004111](https://oeis.org/A004111)). A root carries a *set* of distinct
  subtrees, so B(x) = Σ b(n)xⁿ = x·∏ₖ (1+xᵏ)^b(k), and the OEIS formula for
  the unrooted ones is a(x) = B(x) − (B(x)² + B(x²))/2: a tree is asymmetric
  unless it has a symmetric edge, and B(x²) is the extra count of pairs of
  equal halves.
- Since 1+xᵏ = (1−x²ᵏ)/(1−xᵏ), B(x)/x is the Euler transform of
  w(k) = b(k) − b₂(k), where b₂(k) = b(k/2) for even k and 0 for odd k.
  Taking x·d/dx of the logarithm, as for
  [A000081](../A000081/), gives

  N·b(N+1) = Σ_{e=1..N} e·w(e)·(b(N+1−e) + b(N+1−2e) + ⋯).

- `R` stores b on the even positions only, R[2i] = b(i), with zeros in
  between. Then `R[2e]` is b(e) and `R[e]` is b₂(e) with no parity test
  (an odd e lands on a zero). Each pass appends `0,` and the new b, so while
  a(N) is printed the list is b(0), 0, b(1), 0, …, b(N), of length 2N+1.
- `R[::-1]` pairs position i with 2N−i, so the dot product is
  Σ_j b(j)·b(N−j). In place of b(0) = 0 the list starts with the sentinel
  −1: the j = 0 and j = N terms then add −2·b(N), and
  a(N) = −(Σ_{0<j<N} b(j)b(N−j) − 2b(N) + b₂(N))/2. b₂(N) is the middle
  entry `R[N]`, passed as the start value of `sum`.
- `n` is −N, so `R[-n]` is `R[N]`, and `R=[n:=-1,0,1]` sets the sentinel
  and n = −1 at once.
- In the update `d` runs over −N … −1 (d = −e): `R[-d-d]-R[-d]` is w(e),
  and the slice `R[d-~d:0:d+d]` starts at negative index 2d+1, which is
  position 2(N+1−e), and steps back by 2e: b(N+1−e), b(N+1−2e), …, stopping
  before the sentinel at position 0. The sum is −N·b(N+1), so `//n` gives
  b(N+1).

**Notes**

- Exact integer arithmetic, so the program is right for every n. Both
  divisions are exact: the recurrence's sum is a multiple of N, and the
  printed bracket is even, since the cross terms pair up and the middle
  ones give b(N/2)² + b(N/2).
- Each term costs O(n log n) big-integer operations: the 1000 terms of the
  b-file print in about a second and about 3600 terms in 60 s. The bar is the
  whole b-file in 60 s.
- a(n) ~ 0.2994 · 2.5175ⁿ · n^(−5/2), so from about n = 10750 its decimal
  form passes Python's 4300-digit int-to-str limit.
- The same idea on the plain list b(0), b(1), … costs 149 bytes: the weight
  needs `~d%2*r[-d//2]` and the self pair needs `(j+j==n)` inside the
  convolution. Ending the list with the zero (`R+=X,0`) also gives 149, as the
  reversed slice becomes `R[-2::-1]`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 143 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000220), CC BY-SA 4.0.
