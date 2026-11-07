# A000416

> Number of 6-dimensional partitions of n.
> — [OEIS A000416](https://oeis.org/A000416)

Offset 1: 1, 7, 28, 105, 357, 1197, 3857, 12300, 38430, 118874, …

### Python 3 — 143 bytes

```python
R=range(2,18)
S={frozenset({1})}
while[print(len(S))]:S={s|{p}for s in S for p in{q*r for q in s for r in R}-s if{p//r for r in R if p%r<1}<=s}
```

**How it works**

- A 6-dimensional partition of n is a 6-dimensional array of nonnegative
  integers, weakly decreasing along every axis, with sum n. Stacking
  each entry as a column of cells turns it into an n-cell down-set of
  ℕ⁷ (closed under lowering any coordinate), and back.
- A cell (x₁, …, x₇) is stored as 2^x₁·3^x₂·5^x₃·7^x₄·11^x₅·13^x₆·17^x₇,
  so lowering coordinate i is dividing by the i-th prime, and down-sets
  are sets of 17-smooth numbers closed under dividing by a prime.
- `S` is the set of all down-sets with n cells, as frozensets, starting
  from {{1}} for n = 1. A down-set with n + 1 cells is one with n cells
  plus a cell p ∉ s whose lower neighbours p/r are all in s (remove a
  maximal cell to go back). Such a p is q·r for some q ∈ s and a prime
  r ≤ 17, so `{q*r for q in s for r in R}-s` lists every candidate, the
  filter `{p//r for r in R if p%r<1}<=s` keeps the valid ones, and the
  set comprehension merges the down-sets reached in several ways.
- `R=range(2,18)` also contains composites, which change nothing: if a
  composite r divides p and t is a prime factor of r, then p/r divides
  p/t, so p/r ∈ s already follows from p/t ∈ s for a down-set s; and a
  candidate q·r with r composite is either rejected or a valid cell
  that the primes generate too. It is 4 bytes under listing the 7 primes.
- `print(len(S))` in the header prints a(n) before the next layer is
  built.

**Notes**

- The previous record (164 bytes; 159 with `range(2,18)`) counted each
  down-set once by adding cells in increasing order, `c>max(S)`, in a
  recursive function; it is a little faster (10 terms in 10 s here
  against 9) but longer. Starting from the empty set with `{1,*…}` as in
  [A000293](../A000293/) needs 2 bytes more, since a(0) = a(1) = 1 would
  otherwise be printed twice.
- Exact enumeration with no formula, so the program is right for every n.
- Layer n holds a(n) frozensets: here 7 terms take about 0.4 s and 9
  terms about 6 s. The b-file has 21 terms; the bar is 7 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 266 | first entry |
| 2026-11-06 | Python 3 | 164 | encode cells by prime exponents and enumerate each down-set once |
| 2026-11-07 | Python 3 | 143 | layer by layer as frozensets, `range(2,18)` for the primes |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000416), CC BY-SA 4.0.
