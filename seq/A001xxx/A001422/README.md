# A001422

> Numbers which are not the sum of distinct squares.
> — [OEIS A001422](https://oeis.org/A001422)

Offset 1: 2, 3, 6, 7, 8, 11, 12, 15, 18, 19, 22, 23, 24, 27, 28, 31, 32, 33, 43, 44, 47, …

### Python 3 — 51 bytes

```python
s=1
for n in range(129):s|=s<<n*n;s>>n&1or print(n)
```

**How it works**

- **Subset sums as bits.** Bit j of `s` is set when j is a sum of distinct
  squares among those added so far (the empty sum gives bit 0).
  `s|=s<<n*n` adds n² as an optional new part: every old sum j also gives
  j + n². After the pass for n, s holds all sums of distinct squares from
  0², 1², …, n²; a representation of n only uses squares ≤ n, so bit n is
  already final and the program prints n when it is clear. 0 (the empty sum)
  and 1 are skipped, as in the entry.
- **Why it can stop at 128 (Sprague, 1948: 128 is the largest such
  number).** Self-contained argument: every integer from 129 to
  249 = 128 + 11² is a sum of distinct squares among 1², …, 10² (the same
  bit computation shows it). Induction on k ≥ 10: if every integer in
  [129, X] is a sum of distinct squares ≤ k² and X ≥ 128 + (k+1)², then for
  n in (X, X + (k+1)²], n − (k+1)² lies in [129, X], so n is that sum plus
  (k+1)², a new distinct square. The new interval end X + (k+1)² is again
  ≥ 128 + (k+2)², since (k+1)² ≥ 2k + 3. So every n ≥ 129 is a sum of
  distinct squares, and the 31 numbers printed for n ≤ 128 are the whole
  sequence; the program ends after the last one.
- Exact integer arithmetic.

**Notes**

- The sequence is finite (keyword `fini`, `full`); the bar is all 31 terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 51 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001422), CC BY-SA 4.0.
