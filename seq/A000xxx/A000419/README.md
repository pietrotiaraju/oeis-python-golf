# A000419

> Numbers that are the sum of 3 but no fewer nonzero squares.
> — [OEIS A000419](https://oeis.org/A000419)

Offset 1: 3, 6, 11, 12, 14, 19, 21, 22, 24, 27, …

### Python 3 — 147 bytes

```python
n=1;s={1};t={2};k=2
while 1:
 if n==k*k:s.add(n);t|={n+x for x in s};k+=1
 if n not in s and n not in t and any(n-x in t for x in s):print(n)
 n+=1
```

**How it works**

- `n` scans positive integers, `k` is the next square root to add,
  and s contains exactly {1², 2², …, ⌊√n⌋²} at the membership
  test. When `n==k*k`, insert n and increment k. Signs of square
  roots do not matter, and zero is deliberately absent.

- t contains all sums of two members of s, initially {2}={1+1}.
  When a new largest square n appears, every new pair contains n,
  so add `{n+x for x in s}`. Add n to s first: this includes n+n,
  as required when the same square is used twice.

- `any(n-x in t for x in s)` appends one square to a two-square
  sum. Every square in a representation of n is at most n, so
  this finite test is complete for the current candidate.

- `n not in s and n not in t` excludes one- and two-square
  representations. For example 9=1+4+4 is excluded as a square,
  and 17=4+4+9 is excluded because 17=1+16. In contrast,
  12=4+4+4 passes and requires three nonzero squares.

- Scanning n in increasing order prints each accepted integer once.
  The sets discard duplicate sums: this counts represented values,
  not the number of representations.

**Notes**

- There are ⌊√n⌋ single squares. All stored pair sums are at most
  2n, so their number is O(n); a membership test still tries only
  the ⌊√n⌋ single-square complements.

- Exact integer arithmetic and a complete search over the available
  squares, so the construction remains correct beyond the b-file.
  Time and storage grow with the scanned candidate values.
- This adds the two exclusions to [A000408](../A000408/).
- The b-file has 10000 terms (indices 1 through 10000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 147 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000419), CC BY-SA 4.0.
