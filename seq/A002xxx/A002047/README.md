# A002047

> Number of 3 X (2n+1) zero-sum arrays with entries -n,...,0,...,n.
> — [OEIS A002047](https://oeis.org/A002047)

Offset 0: 1, 2, 6, 28, 244, 2544, 35600, 659632, 15106128, 425802176, 14409526080, 577386122880, 27029459961728, 1462450710036480, …

### Python 3 — 120 bytes

```python
f=lambda i,V,A:i>n or sum(f(i+1,V-{v},A-{i+v})for v in V if i+v in A)
n=0
while[print(f(-n,R:={*range(-n,n+1)},R))]:n+=1
```

**How it works**

- **The definition.** An m × (2n+1) zero-sum array (Gheorghe Coserea's
  comment on the entry) has rows that are permutations of −n, …, n, every
  column summing to 0, and first row −n, −n+1, …, n in this order. With
  three rows, column i holds i, σ(i) and −i−σ(i), where σ is the second
  row. The third row is a permutation of −n, …, n exactly when the column
  sums i + σ(i) of the first two rows are all different and lie in
  −n, …, n. So a(n) counts the permutations σ of {−n, …, n} with that
  property, and the program counts them directly.
- **The search.** `f(i,V,A)` counts the ways to fill columns i, …, n when
  `V` holds the second-row values not used yet and `A` the sums
  i + σ(i) not used yet (the negated third-row values). Column i may take
  any v in V with i + v in A, which removes v from V and i + v from A.
  Past the last column (`i>n`) one array is complete and the lambda
  returns True, which `sum` counts as 1. Both sets start as
  {−n, …, n}, so one set `R` is passed twice.
- Every permutation is reached once (column by column, each choice
  recorded in V and A), so `f(-n,R,R)` is a(n) for every n, including
  a(0) = 1 (the 3 × 1 array of zeros).

**Notes**

- Exact integer counting with no theorem beyond the definition. The search
  visits each valid partial array once, so its time grows about like
  a(n) itself: n = 6 (35600 arrays) takes under 2 s and n = 7 (659632)
  about 50 s on a slow PC, while n = 8 (15106128) would take about twenty minutes.
  The bar is 8 terms (n = 0 to 7) with a 120 s timeout.
- Swapping the second and third rows (σ(i) ↔ −i−σ(i)) pairs the arrays,
  so a(n) is even for n ≥ 1; the search does not use it.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 120 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002047), CC BY-SA 4.0.
