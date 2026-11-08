# A001066

> Dimensions (sorted, with duplicates removed) of real simple Lie algebras.
> — [OEIS A001066](https://oeis.org/A001066)

Offset 1: 3, 6, 8, 10, 14, 15, 16, 20, 21, 24, 28, 30, 35, 36, 42, 45, 48, 52, 55, 56, …

### Python 3 — 117 bytes

```python
Q={-14,-52,-133,-248};k=n=0
while[{n+1,2*n+4,8*n+1,4*n-~(n<13),-n,-n/2}&Q and print(n)]:n+=1;Q|={(k:=k+(k*k<9*n))**2}
```

**How it works**

- **Which dimensions.** A real simple Lie algebra is either a real form of
  a complex simple algebra g (same dimension, dim g) or a complex simple g
  seen as a real algebra (dimension 2·dim g). So the terms are the numbers
  d and 2d for d in the complex list [A003038](https://oeis.org/A003038):
  Aₖ: k(k+2) for k ≥ 1, Bₖ and Cₖ: k(2k+1), Dₖ: k(2k−1), and G₂, F₄, E₆,
  E₇, E₈ = 14, 52, 78, 133, 248.
- **The classical series as square tests.** k(k+2) = j² − 1 with j = k+1,
  so d is in Aₖ iff d+1 is a square (d ≥ 3). k(2k+1) and k(2k−1) are the
  triangular numbers T₂ₖ and T₂ₖ₋₁, and Bₖ (k ≥ 2), Cₖ (k ≥ 3), Dₖ (k ≥ 4)
  together with A₃ = 15 cover every T_m with m ≥ 4, and n is triangular
  iff 8n+1 is a square. Doubling: n = 2(j²−1) iff 2n+4 = (2j)², and
  n = 2T_m = m(m+1) iff 4n+1 = (2m+1)².
- So n is a term iff one of n+1, 2n+4, 8n+1, 4n+1 is a perfect square, or n
  is 14, 52, 133, 248 or twice one of them, with three small corrections:
  n = 1 (8n+1 = 9, T₁) and n = 2 and 12 (4n+1 = 9 and 49, twice T₁ and
  T₃) are not terms. `4*n-~(n<13)` adds 1 below 13, where 4n+2 is never a
  square; n = 1 is dropped by the lag described below. The square tests
  catch T₂ = 3 and T₃ = 6 too, but those are terms anyway (3 = A₁,
  6 = 2·A₁). E₆ = 78 = T₁₂ and 2·248 = 496 = T₃₁ need no entry of their
  own.
- **One set lookup.** `Q` holds the squares found so far and the negated
  exceptional dimensions. The six numbers n+1, 2n+4, 8n+1, 4n+1, −n and
  −n/2 go in a set, and `&Q` is non-empty exactly when one of them is a
  square in `Q` or −n or −n/2 is one of −14, −52, −133, −248 (−n/2 is a
  float, equal to an int only for even n; squares are positive, so the
  two kinds never mix). `…&Q and print(n)` prints n then, and
  `while[…]:n+=1` moves on.
- **Squares on the fly.** Each step adds k² to `Q` and raises k by 1 while
  k² < 9n (`k+(k*k<9*n)`; when k does not move, the same square goes in
  again). Since 9n grows by 9 a step and the gap between squares is
  2k+1 ≥ 9 once k ≥ 4, k² ≥ 9n holds for good from n = 10 on, so every
  square up to 9n > 8n+1 is in `Q` and the tests are exact. Below 10, k
  lags: at n = 1 the square 9 is not in `Q` yet, which is what keeps 1 out,
  and no term is lost (3, 6, 8 are caught by n+1 or 2n+4). `Q` keeps only
  about 3√n squares.

**Notes**

- Exact integer arithmetic (`n/2` only meets four small integers).
- The b-file has 10000 terms (up to 5918520); they print in about 20–35 s
  on this PC depending on load, and the bar is the whole b-file.
- The first entry (128 bytes) tested each number with `math.isqrt` in a
  generator: `0in(math.isqrt(x)**2-x for x in(n+1,2*n+4,8*n+1,4*n-~(n<13)))`
  `or{n,n/2}&{14,52,133,248}`. The set of squares is 11 bytes shorter and
  faster.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 128 | first entry |
| 2026-11-08 | Python 3 | 117 | squares kept in a set with the exceptional dimensions negated; one `&` per number |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001066), CC BY-SA 4.0.
