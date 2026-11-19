# A002048

> Segmented numbers, or prime numbers of measurement.
> — [OEIS A002048](https://oeis.org/A002048)

Offset 1: 1, 2, 4, 5, 8, 10, 14, 15, 16, 21, 22, 25, 26, 28, 33, 34, 35, 36, 38, …

### Python 3 — 70 bytes

```python
k=s=0;P={0}
while k:=k+1:{k+p for p in P}&P or[print(k),P.add(s:=s+k)]
```

**How it works**

- The segmented numbers are the positive integers that are not the sum
  of two or more consecutive smaller terms (the entry's comment). P
  holds the prefix sums 0, a(1), a(1) + a(2), … of the terms found so
  far, and s the last of them.
- A block of consecutive terms sums to k exactly when two prefix sums
  differ by k, that is, when k + p is in P for some p in P. Every term
  found so far is smaller than k, so such a block cannot be a single
  term: it has two or more, as the definition asks.
- So k is a term when the set {k + p : p in P} misses P. Then
  `[print(k),P.add(s:=s+k)]` (a true list, evaluated only after `or`)
  prints it and adds the new prefix sum.

**Notes**

- The same program printing s instead of k gives the partial sums,
  [A002049](../A002049/).
- Exact integer arithmetic, so the program is right for every n. Each
  candidate costs one pass over P, so the run time grows like the
  square of the number of terms.
- The b-file has 10000 terms, up to 39129. The bar is 9000 terms in
  60 s; they take about 28 s here, and the whole b-file about 35 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002048), CC BY-SA 4.0.
