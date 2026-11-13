# A001574

> Colored series-parallel networks.
> — [OEIS A001574](https://oeis.org/A001574)

Offset 1: 0, 2, 12, 60, 292, 1438, 7180, 36566

### Python 3 — 122 bytes

```python
A=[1,2];B=[1,n:=1]
while[print(A[n]-2*B[n])]:
 n+=1
 for X in A,B:X+=sum(sum(X[-d::-d])*d*X[d]for d in(1,*range(1,n)))//n,
```

**How it works**

- **The definition.** The entry only cites Riordan (*An Introduction
  to Combinatorial Analysis*, 1958, p. 159). Reading it as
  series-parallel networks with n edges, each edge painted one of 2
  colors, that use **both** colors, reproduces all 8 terms;
  [A001575](../A001575/) is the same with exactly 3 colors.
- **Networks with k colors.** Let N_k(n) count series-parallel
  networks with n edges, each in one of k colors (k = 1 is
  [A000084](../../A000xxx/A000084/)). As in Riordan and Shannon's
  count, a network with n ≥ 2 edges is either a series or a parallel
  connection, and the duality that swaps the two keeps the colors, so
  each kind is N_k(n)/2. A network is a multiset of non-parallel parts
  (single edges, k kinds, or series networks) connected in parallel,
  so 1 + Σ N_k(n)xⁿ = Π_n (1 − xⁿ)^(−b(n)) with b(1) = k and
  b(n) = N_k(n)/2 for n ≥ 2.
- **The recurrence.** The Euler transform gives
  n·N(n) = Σ_(d≤n) d·b(d)·Σ_(j≥1) N(n − jd) with N(0) = 1; the d = n
  term is n·N(n)/2, so n·N(n) = Σ_(d<n) 2d·b(d)·Σ_(j≥1) N(n − jd).
  That is A000084's program with the list started at [1, k]: for
  d ≥ 2 the weight 2d·b(d) is d·N(d), and for d = 1 it is
  2k = 2·N(1), which the tuple `(1,*range(1,n))` gets by running d = 1
  twice. The slice `X[-d::-d]` is N(n − d), N(n − 2d), …, N(0).
- **Exactly two colors.** A network with colors from a 2-set uses both,
  one or none of them, so N₂(n) = E(n) + 2·N₁(n) for n ≥ 1, and
  a(n) = N₂(n) − 2·N₁(n). `A` holds N₂ and `B` holds N₁; the inner
  `for` extends both lists in place.

**Notes**

- Exact integer arithmetic (each sum is n·N(n), so `//n` is exact),
  so the program is right for every n.
- The 8 terms fit in a table shorter than the program, so it needs a
  review. It prints them at once and goes on (a(9) = 189296,
  a(10) = 995514); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 122 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001574), CC BY-SA 4.0.
