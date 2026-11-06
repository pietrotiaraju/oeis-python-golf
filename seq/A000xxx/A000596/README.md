# A000596

> Central factorial numbers: A008955(n,2).
> — [OEIS A000596](https://oeis.org/A000596)

Offset 3: 4, 49, 273, 1023, 3003, 7462, 16422, 32946, 61446, 108031, …

### Python 3 — 47 bytes

```python
n=a=1;b=0
while 1:n+=1;b+=n*n*a;a+=n*n;print(b)
```

**How it works**

- `n` is the largest square processed, `a` is the sum of those
  squares, and `b` is their elementary symmetric sum of order 2.
  Initially only 1² is present, so n=a=1 and b=0.
- Adding n² creates exactly n²·a new pairs. Update `b` before adding
  n² to `a`, so the new square is never paired with itself.
- The loop first processes 2² and prints 4. After processing m² the
  result is the sum over 1²,…,m², corresponding to the OEIS index
  m+1 and its initial offset 3.

**Notes**

- Only a fixed number of counters are stored. This avoids the larger
  explicit degree polynomial and performs no divisions.
- The reference file contains 9998 terms from the OEIS b-file; the verification
  bar is 9998 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000596), CC BY-SA 4.0.
