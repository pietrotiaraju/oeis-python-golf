# A000542

> Sum of 8th powers: 1^8 + 2^8 + ... + n^8.
> — [OEIS A000542](https://oeis.org/A000542)

Offset 0: 0, 1, 257, 6818, 72354, 462979, 2142595, 7907396, 24684612, 67731333, …

### Python 3 — 34 bytes

```python
n=a=0
while[print(a)]:n+=1;a+=n**8
```

**How it works**

- Maintain a(n)=Σₖ₌₀ⁿ k^8. The empty initial contribution is 0.
  Advancing n adds precisely the new summand n^8.
- Printing before the update includes the offset n=0 and avoids a
  separate initial print.
- This running sum is shorter than the corresponding Faulhaber
  polynomial, and it needs only an index and an accumulator.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 24 terms from the published OEIS entry; the verification
  bar is 24 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000542), CC BY-SA 4.0.
