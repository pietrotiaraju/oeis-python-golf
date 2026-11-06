# A000404

> Numbers that are the sum of 2 nonzero squares.
> — [OEIS A000404](https://oeis.org/A000404)

Offset 1: 2, 5, 8, 10, 13, 17, 18, 20, 25, 26, …

### Python 3 — 91 bytes

```python
n=1;s={1};k=2
while 1:
 if n==k*k:s.add(n);k+=1
 if any(n-x in s for x in s):print(n)
 n+=1
```

**How it works**

- `n` scans positive integers, `k` is the next square root to add,
  and s contains exactly {1², 2², …, ⌊√n⌋²} at the membership
  test. When `n==k*k`, insert n and increment k. Signs of square
  roots do not matter, and zero is deliberately absent.

- `any(n-x in s for x in s)` asks whether n is the sum of two
  positive squares. Every square in a representation is at most n,
  so the current s contains every square needed for the test.

- Scanning n in increasing order prints each accepted integer once.
  The sets discard duplicate sums: this counts represented values,
  not the number of representations.

**Notes**

- The set has ⌊√n⌋ entries and a test tries at most that many
  complements. Maintaining the next square avoids recomputing
  integer square roots for each candidate.

- Exact integer arithmetic and a complete search over the available
  squares, so the construction remains correct beyond the b-file.
  Time and storage grow with the scanned candidate values.
- Compare [A000415](../A000415/), which also excludes single squares.
- The b-file has 10000 terms (indices 1 through 10000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 91 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000404), CC BY-SA 4.0.
