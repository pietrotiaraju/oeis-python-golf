# A000597

> Central factorial numbers: A008955(n,3).
> — [OEIS A000597](https://oeis.org/A000597)

Offset 4: 36, 820, 7645, 44473, 191620, 669188, 1999370, 5293970, 12728936, 28285400, …

### Python 3 — 62 bytes

```python
n=2;a=5;b=4;c=0
while 1:n+=1;c+=n*n*b;b+=n*n*a;a+=n*n;print(c)
```

**How it works**

- `a`, `b`, and `c` are the elementary symmetric sums of orders
  1, 2, and 3 in the squares already processed. Initially these are
  5, 4, and 0 for the set {1²,2²}, with n=2.
- On adjoining n², each new triple contributes n² times an old pair,
  and each new pair contributes n² times an old single square.
  Updating `c`, then `b`, then `a` preserves these old values.
- The first new square is 3² and the first triple product is 36.
  After processing m² the output has OEIS index m+1, starting at 4.

**Notes**

- Only a fixed number of counters are stored. This avoids the larger
  explicit degree polynomial and performs no divisions.
- The reference file contains 997 terms from the OEIS b-file; the verification
  bar is 997 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 62 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000597), CC BY-SA 4.0.
