# A000541

> Sum of 7th powers: 1^7 + 2^7 + ... + n^7.
> — [OEIS A000541](https://oeis.org/A000541)

Offset 0: 0, 1, 129, 2316, 18700, 96825, 376761, 1200304, 3297456, 8080425, …

### Python 3 — 34 bytes

```python
n=a=0
while[print(a)]:n+=1;a+=n**7
```

**How it works**

- Maintain a(n)=Σₖ₌₀ⁿ k^7. The empty initial contribution is 0.
  Advancing n adds precisely the new summand n^7.
- Printing before the update includes the offset n=0 and avoids a
  separate initial print.
- This running sum is shorter than the corresponding Faulhaber
  polynomial, and it needs only an index and an accumulator.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 1001 terms from the OEIS b-file; the verification
  bar is 1001 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000541), CC BY-SA 4.0.
