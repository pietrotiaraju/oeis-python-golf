# A002049

> Prime numbers of measurement.
> — [OEIS A002049](https://oeis.org/A002049)

Offset 1: 1, 3, 7, 12, 20, 30, 44, 59, 75, 96, 118, 143, 169, 197, 230, 264, 299, …

### Python 3 — 70 bytes

```python
k=s=0;P={0}
while k:=k+1:{k+p for p in P}&P or[P.add(s:=s+k),print(s)]
```

**How it works**

- The terms are the partial sums of the segmented numbers
  [A002048](../A002048/): the positive integers that are not the sum of
  two or more consecutive smaller segmented numbers. P holds the prefix
  sums found so far, starting with 0, and s the last of them.
- A block of consecutive segmented numbers sums to k exactly when two
  prefix sums differ by k, that is, when k + p is in P for some p in P;
  every one found so far is smaller than k, so the block has at least
  two members, as the definition asks.
- So k is a segmented number when {k + p : p in P} misses P; then
  `[P.add(s:=s+k),print(s)]` adds k to the running sum, stores it in P
  and prints it.

**Notes**

- Exact integer arithmetic, so the program is right for every n. Each
  candidate costs one pass over P, so the run time grows like the
  square of the number of terms.
- The b-file has 10000 terms, up to 188286782. The bar is 9000 terms
  in 60 s; they take about 28 s here, and the whole b-file about 35 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002049), CC BY-SA 4.0.
