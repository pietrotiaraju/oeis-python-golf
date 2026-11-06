# A000570

> Number of tournaments on n nodes determined by their score vectors.
> — [OEIS A000570](https://oeis.org/A000570)

Offset 1: 1, 1, 2, 4, 7, 11, 18, 31, 53, 89, …

### Python 3 — 54 bytes

```python
A=[1,1,2,4,7]
while[print(A[0])]:A=A[1:]+[sum(A)-A[3]]
```

**How it works**

- The OEIS recurrence is a(n)=a(n−1)+a(n−3)+a(n−4)+a(n−5),
  with a(1),…,a(5)=[1,1,2,4,7]. These initial values are the boundary
  conditions of that recurrence.
- `A` is a window of five consecutive terms. Its next term is the sum
  of all five except A[3], the coefficient of a(n−2), which is zero.
- Printing the oldest value before shifting the window preserves the
  offset and uses constant storage.

**Notes**

- Every term is computed with exact integer arithmetic.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 500 terms from the OEIS b-file; the verification
  bar is 500 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000570), CC BY-SA 4.0.
