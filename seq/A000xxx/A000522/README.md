# A000522

> Total number of ordered k-tuples (k=0..n) of distinct elements from an n-element set: a(n) = Sum_{k=0..n} n!/k!.
> — [OEIS A000522](https://oeis.org/A000522)

Offset 0: 1, 2, 5, 16, 65, 326, 1957, 13700, 109601, 986410, …

### Python 3 — 36 bytes

```python
n=0;a=1
while[print(a)]:n+=1;a=n*a+1
```

**How it works**

- a(n)=Σₖ₌₀ⁿ n!/k!. Multiplying a(n−1) by n produces every term of
  this sum except the final 1, giving a(n)=n·a(n−1)+1.
- The empty set contributes a(0)=1. The loop prints before incrementing
  n, so the offset and the initial value are both included.
- A single accumulator suffices; neither factorials nor the individual
  tuple lengths need to be stored.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 451 terms from the OEIS b-file; the verification
  bar is 451 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000522), CC BY-SA 4.0.
