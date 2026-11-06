# A000423

> a(n) is smallest number > a(n-1) of form a(i)*a(j), i < j < n.
> — [OEIS A000423](https://oeis.org/A000423)

Offset 1: 2, 3, 6, 12, 18, 24, 36, 48, 54, 72, …

### Python 3 — 79 bytes

```python
a=[];s={2,3}
while s:
 n=min(s);s.remove(n);print(n);s|={n*x for x in a};a+=[n]
```

**How it works**

- a holds the terms already printed. The frontier s contains the seeds
  2 and 3 until used, together with all distinct products of two
  different earlier positions that have not yet been printed.
- Choose `n=min(s)`, remove it, and print it. Every newly available
  product uses this n and one old term, so `s|={n*x for x in a}`
  adds exactly the new possibilities.
- Append n to a only after forming those products. This enforces i<j:
  the program cannot form n·n using the same position twice. A square
  can still be allowed if two different sequence values multiply to it.
- Every factor is at least 2. New products therefore exceed n and
  cannot disturb the increasing order. A set merges products reached
  in different ways, so no value is printed twice.
- The seeds print first, then 6=2·3, 12=2·6 and 18=3·6.
  Neither 4=2² nor 9=3² is initially available under the distinct-index
  rule.

**Notes**

- The frontier remains nonempty: after the seeds, the old term 2
  always supplies a future product 2n. Each pass therefore implements
  the defining least-available-product rule indefinitely.
- Exact integer products, without a cutoff on candidate size. Through
  N outputs, N(N−1)/2 pairs have been formed before deduplication;
  the frontier and repeated `min` scans are the main storage and time
  costs.
- Keeping the frontier avoids repeatedly scanning every integer and
  testing whether it factors into two previous terms.
- The b-file has 49 terms (indices 1 through 49). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000423), CC BY-SA 4.0.
