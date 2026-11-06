# A000447

> a(n) = 1^2 + 3^2 + 5^2 + 7^2 + ... + (2*n-1)^2 = n*(4*n^2 - 1)/3.
> — [OEIS A000447](https://oeis.org/A000447)

Offset 0: 0, 1, 10, 35, 84, 165, 286, 455, 680, 969, …

### Python 3 — 35 bytes

```python
s=0;n=1
while[print(s)]:s+=n*n;n+=2
```

**How it works**

- At the m-th output, s is the sum of the first m odd squares,
  and n=2m+1 is the next odd integer. Initially m=0, s=0 and n=1,
  so the empty sum is printed first.
- The body adds n² and then advances n by 2, preserving both
  invariants. For example, after printing 1, it adds 3² to obtain
  10; after printing 10 it adds 5² to obtain 35.
- The closed form follows by summing (2j−1)²:
  a(m)=4Σj²−4Σj+m=m(4m²−1)/3.
  The program uses the defining partial sum instead, avoiding a
  multiplication by a polynomial and a division in the output.

**Notes**

- Exact integer additions and multiplications; the proof uses the
  definition, so there is no reliance on a finite difference fit.
- `[print(s)]` is always a nonempty list. This puts the output at
  the start of the loop without a separate `while 1:` print statement.
- Only the sum and next odd integer are stored. Their bit lengths grow
  logarithmically with the term index; printing increasingly large
  values eventually costs more than the fixed number of updates.
- [A000466](../A000466/) evaluates the related factor 4m²−1
  directly, while this sequence includes the extra m/3 factor.
- The b-file has 1001 terms (indices 0 through 1000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000447), CC BY-SA 4.0.
