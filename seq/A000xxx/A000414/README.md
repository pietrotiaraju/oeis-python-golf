# A000414

> Numbers that are the sum of 4 nonzero squares.
> — [OEIS A000414](https://oeis.org/A000414)

Offset 1: 4, 7, 10, 12, 13, 15, 16, 18, 19, 20, …

### Python 3 — 143 bytes

```python
n=1;s={1};t={2};u={3};k=2
while 1:
 if n==k*k:s.add(n);t|={n+x for x in s};u|={n+x for x in t};k+=1
 if any(n-x in u for x in s):print(n)
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

- u similarly holds all sums of three available squares, initially
  {3}. Its update adds n+x for x in the already updated t. This
  includes triples using the new square once, twice or three times;
  every new triple is generated because its largest square is n.

- `any(n-x in u for x in s)` appends a fourth square. Although
  t and u also store sums larger than n, only n−x is queried;
  these future sums cannot create a false positive.

- Scanning n in increasing order prints each accepted integer once.
  The sets discard duplicate sums: this counts represented values,
  not the number of representations.

**Notes**

- There are ⌊√n⌋ single squares. All stored pair sums are at most
  2n, so their number is O(n); a membership test still tries only
  the ⌊√n⌋ single-square complements.

- Triple sums are at most 3n, so u also has O(n) entries. Updating
  it only at square candidates reuses the sums between those updates.

- Exact integer arithmetic and a complete search over the available
  squares, so the construction remains correct beyond the b-file.
  Time and storage grow with the scanned candidate values.
- The four-square theorem permits zero squares; this program enforces four nonzero ones.
- The b-file has 10000 terms (indices 1 through 10000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 143 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000414), CC BY-SA 4.0.
