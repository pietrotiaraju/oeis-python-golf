# A000567

> Octagonal numbers: n*(3*n-2). Also called star numbers.
> — [OEIS A000567](https://oeis.org/A000567)

Offset 0: 0, 1, 8, 21, 40, 65, 96, 133, 176, 225, …

### Python 3 — 32 bytes

```python
n=0
while[print(n*(3*n-2))]:n+=1
```

**How it works**

- Evaluate the octagonal-number formula n(3n−2) from n=0,
  including the initial zero. All terms are integers directly.
- The first differences are 1, 7, 13, …, increasing by 6 at each
  step, as expected for successive layers of octagonal numbers.
- Printing inside a nonempty list keeps the loop running and allows
  the index update to follow in the same statement.

**Notes**

- Every term is computed with exact integer arithmetic.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 1001 terms from the OEIS b-file; the verification
  bar is 1001 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 32 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000567), CC BY-SA 4.0.
