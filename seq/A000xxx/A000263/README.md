# A000263

> Number of partitions into non-integral powers.
> — [OEIS A000263](https://oeis.org/A000263)

Offset 3: 3, 14, 39, 91, 173, 307, 502, 779, 1150, 1651, 2280, …

a(n) counts the pairs of integers 1 ≤ x < y with √x + √y ≤ n
(R. J. Mathar's comment on the entry).

### Python 3 — 60 bytes

```python
n=3
while[print(sum(k*k//4//n//n for k in range(n*n)))]:n+=1
```

**How it works**

- **The formula.** a(n) = Σ_{k=0}^{n²−1} ⌊k² / (4n²)⌋, so no square root is
  ever taken.
- **Why.** Write N = n² and y = x + d with d ≥ 1. Then √(x+d) ≤ n − √x is
  the same as x + d ≤ N − 2n√x + x, that is 2n√x ≤ N − d, and since both
  sides are then non-negative it is the same as N − d ≥ 0 and
  4Nx ≤ (N − d)². (This also gives √x < n/2, so n − √x ≥ 0 was not lost.)
  For d ≥ N there is no x ≥ 1 at all; for 1 ≤ d ≤ N − 1 the good x are
  1, …, ⌊(N − d)² / 4N⌋. Summing over d and putting k = N − d gives
  Σ_{k=1}^{N−1} ⌊k² / 4N⌋. The k = 0 term is 0, so `range(n*n)` can start
  at 0.
- **Exactness.** For positive integers p and q, ⌊⌊x/p⌋/q⌋ = ⌊x/(pq)⌋, so
  `k*k//4//n//n` is exactly ⌊k²/(4n²)⌋; everything is integer arithmetic.
- **The loop.** `print` sits in the loop condition: it returns `None`, and
  `[None]` is a non-empty list, so the loop never ends (the
  [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms:
  - with m = 2n, `m=6` and `while[print(sum(k*k//m//m for k in range(m*m>>2)))]:m+=2`:
    also 60 bytes (`k*k//n//n>>2` is the same length as `k*k//4//n//n` too);
  - one term per x, a(n) = Σ_x max(0, n² − ⌈2n√x⌉) with
    ⌈√m⌉ = isqrt(m − 1) + 1, `from math import*` and
    `sum(max(0,n*n+~isqrt(4*n*n*x-1))for x in range(1,n*n))`: 95 bytes;
  - counting the pairs directly with the exact test
    `(n*n+x-y)**2>=4*n*n*x` over 1 ≤ x < y < n²: 88 bytes, but O(n⁴) per term
    (63 terms in 60 s here).
- Exact integer arithmetic; correctness for every n rests only on the
  derivation above, nothing is conjectural. The values were checked against
  the per-x isqrt count for n = 3..299 and against a direct pair count for
  n = 3..14.
- Each term costs n² steps: here the program prints about 730 terms in 60 s.
  The b-file has 36 terms (up to a(38), synthesized from the entry's data)
  and all of them print in well under a second; the bar is the whole b-file
  in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 60 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000263), CC BY-SA 4.0.
