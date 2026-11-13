# A001575

> Colored series-parallel networks.
> — [OEIS A001575](https://oeis.org/A001575)

Offset 1: 0, 0, 8, 102, 948, 7900, 62928, 491832

### Python 3 — 139 bytes

```python
A=[1,3];B=[1,2];C=[1,n:=1]
while[print(A[n]-3*B[n]+3*C[n])]:
 n+=1
 for X in A,B,C:X+=sum(sum(X[-d::-d])*d*X[d]for d in(1,*range(1,n)))//n,
```

**How it works**

- **The definition.** The entry only cites Riordan (*An Introduction
  to Combinatorial Analysis*, 1958, p. 159). Reading it as
  series-parallel networks with n edges, each edge painted one of 3
  colors, that use **all three** colors, reproduces all 8 terms;
  [A001574](../A001574/) is the same with exactly 2 colors, and its
  page derives the count N_k(n) of networks whose edges take k colors:
  A000084's Euler-transform program with the list started at [1, k].
- **Exactly three colors.** Sorting the networks with colors from a
  3-set by the set of colors they use gives
  N₃ = E₃ + 3E₂ + 3E₁ and N₂ = E₂ + 2E₁, N₁ = E₁ (n ≥ 1), so by
  inclusion–exclusion a(n) = E₃(n) = N₃(n) − 3N₂(n) + 3N₁(n).
- **The lists.** `A`, `B`, `C` hold N₃, N₂, N₁ and start as [1, 3],
  [1, 2], [1, 1]; the inner `for` extends all three in place with
  n·N(n) = Σ d·N(d)·Σ_(j≥1) N(n − jd) over d = 1, 1, 2, …, n − 1 (the
  doubled d = 1 term supplies the weight 2·b(1) = 2k).

**Notes**

- Exact integer arithmetic (each sum is n·N(n), so `//n` is exact),
  so the program is right for every n.
- The 8 terms fit in a table shorter than the program, so it needs a
  review. It prints them at once and goes on (a(9) = 3817716,
  a(10) = 29614782); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 139 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001575), CC BY-SA 4.0.
